"""Command-line demonstration of the shared public translation pipeline."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from app.pipeline import DemoTranslator, SessionMemory, load_glossary, process_text

def main()->None:
    glossary=load_glossary(ROOT/'data/glossary_sample.json'); translator=DemoTranslator(); memory=SessionMemory(max_segments=5)
    samples=[('오늘 말씀을 통해 하나님의 은혜를 기억합니다.',True),('아직 이어지는',False),('우리는 서로를 사랑해야 합니다.',True)]
    for text,is_final in samples:
        segment=process_text(text,is_final=is_final,glossary=glossary,translator=translator); memory.add(segment); print(segment.to_dict())
    print('\nViewer-ready session:')
    for segment in memory.items(): print(f"- {segment['translated_text']}")

if __name__=='__main__': main()
