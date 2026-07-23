"""FastAPI and WebSocket demo for the public translation portfolio."""
from __future__ import annotations
import asyncio
from pathlib import Path
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from .pipeline import DemoTranslator, SessionMemory, load_glossary, process_text

ROOT=Path(__file__).resolve().parents[1]
app=FastAPI(title='Church Live Translation Portfolio Demo',version='1.0.0')
memory=SessionMemory(max_segments=8); glossary=load_glossary(ROOT/'data/glossary_sample.json'); translator=DemoTranslator(); clients:set[WebSocket]=set(); lock=asyncio.Lock()

class ProcessRequest(BaseModel):
    source_text:str=Field(min_length=1,max_length=1000)
    is_final:bool=True

async def broadcast(payload:dict)->None:
    disconnected=[]
    async with lock:
        for ws in clients:
            try: await ws.send_json(payload)
            except Exception: disconnected.append(ws)
        for ws in disconnected: clients.discard(ws)

@app.get('/health')
def health()->dict: return {'status':'ok','mode':'synthetic-demo'}

@app.get('/api/segments')
def segments()->dict: return {'segments':memory.items()}

@app.post('/api/process')
async def process(request:ProcessRequest)->dict:
    segment=process_text(request.source_text,is_final=request.is_final,glossary=glossary,translator=translator); memory.add(segment); payload={'type':'segment','segment':segment.to_dict()}; await broadcast(payload); return payload

@app.post('/api/session/clear')
async def clear_session()->dict:
    memory.clear(); payload={'type':'session_cleared','segments':[]}; await broadcast(payload); return payload

@app.websocket('/ws')
async def websocket_endpoint(websocket:WebSocket)->None:
    await websocket.accept()
    async with lock: clients.add(websocket)
    await websocket.send_json({'type':'session_snapshot','segments':memory.items()})
    try:
        while True:
            if (await websocket.receive_text()).lower()=='ping': await websocket.send_text('pong')
    except WebSocketDisconnect:
        async with lock: clients.discard(websocket)

@app.get('/',response_class=HTMLResponse)
def viewer()->str:
    return '''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Live Translation Demo</title><style>body{font-family:Arial;max-width:900px;margin:auto;padding:24px;background:#101827;color:#f5f7fb}.panel{background:#1d2939;border:1px solid #344054;border-radius:12px;padding:18px;margin:16px 0}textarea{width:100%;min-height:90px;padding:12px;box-sizing:border-box}button{padding:10px 14px;margin:8px 8px 0 0}.segment{border-left:4px solid #53b1fd;padding:10px 14px;margin:12px 0;background:#182230}.source{color:#98a2b3}.status{float:right;color:#fdb022}</style></head><body><h1>Korean–English Live Translation Demo</h1><p>Fictional model-agnostic demonstration. No microphone, recording, transcript, or production model is connected.</p><div class="panel"><textarea id="source">오늘 말씀을 통해 하나님의 은혜를 기억합니다.</textarea><button onclick="send(true)">Send final</button><button onclick="send(false)">Send partial</button><button onclick="clearSession()">Clear</button></div><div class="panel"><h2>Viewer session</h2><div id="segments"></div></div><script>const box=document.getElementById('segments');function render(items){box.innerHTML=items.map(s=>`<div class="segment"><span class="status">${s.status}</span><div class="source">${s.cleaned_source}</div><div>${s.translated_text||'(suppressed)'}</div></div>`).join('')}async function refresh(){const r=await fetch('/api/segments');render((await r.json()).segments)}async function send(is_final){await fetch('/api/process',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({source_text:document.getElementById('source').value,is_final})})}async function clearSession(){await fetch('/api/session/clear',{method:'POST'})}const protocol=location.protocol==='https:'?'wss':'ws';const ws=new WebSocket(`${protocol}://${location.host}/ws`);ws.onmessage=e=>{const d=JSON.parse(e.data);if(d.type==='session_snapshot'||d.type==='session_cleared')render(d.segments);else refresh()};refresh();</script></body></html>'''
