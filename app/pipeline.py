"""Model-agnostic translation pipeline for the public portfolio demo."""
from __future__ import annotations
from collections import deque
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping
import json, re, uuid

DEFAULT_CORRECTIONS={"하나님의 은에":"하나님의 은혜","성경 말슴":"성경 말씀","배들레헴":"베들레헴"}
DEFAULT_TRANSLATIONS={
    "오늘 말씀을 통해 하나님의 은혜를 기억합니다.":"Through today's message, we remember God's grace.",
    "우리는 서로를 사랑해야 합니다.":"We should love one another.",
    "믿음으로 한 걸음 나아갑시다.":"Let us take one step forward in faith.",
}

@dataclass(frozen=True)
class TranslationSegment:
    segment_id:str
    timestamp:str
    raw_source:str
    cleaned_source:str
    translated_text:str
    glossary_matches:tuple[str,...]
    status:str
    def to_dict(self)->dict:
        result=asdict(self); result['glossary_matches']=list(self.glossary_matches); return result

class SessionMemory:
    def __init__(self,max_segments:int=8)->None:
        if max_segments<1: raise ValueError('max_segments must be at least 1.')
        self._segments:deque[TranslationSegment]=deque(maxlen=max_segments)
    def add(self,segment:TranslationSegment)->None:
        if segment.status=='final': self._segments.append(segment)
    def clear(self)->None: self._segments.clear()
    def items(self)->list[dict]: return [segment.to_dict() for segment in self._segments]

class DemoTranslator:
    """Deterministic adapter used instead of a production model."""
    def __init__(self,translations:Mapping[str,str]|None=None)->None: self.translations=dict(translations or DEFAULT_TRANSLATIONS)
    def translate(self,source:str)->str: return self.translations.get(source,f'[Demo translation] {source}')

def load_glossary(path:Path)->dict[str,str]:
    data=json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data,dict) or not all(isinstance(k,str) and isinstance(v,str) for k,v in data.items()): raise ValueError('Glossary must be a JSON object of string pairs.')
    return data

def clean_source(text:str,corrections:Mapping[str,str])->str:
    normalized=re.sub(r'\s+',' ',text).strip()
    for incorrect,corrected in corrections.items(): normalized=normalized.replace(incorrect,corrected)
    return normalized

def glossary_matches(text:str,glossary:Mapping[str,str])->tuple[str,...]:
    return tuple(f'{source} → {target}' for source,target in glossary.items() if source in text)

def process_text(text:str,*,is_final:bool,glossary:Mapping[str,str],translator:DemoTranslator,
                 corrections:Mapping[str,str]|None=None,now:datetime|None=None)->TranslationSegment:
    cleaned=clean_source(text,corrections or DEFAULT_CORRECTIONS); displayable=is_final and len(cleaned)>=4
    return TranslationSegment(str(uuid.uuid4()),(now or datetime.now(timezone.utc)).isoformat(timespec='seconds'),text,cleaned,translator.translate(cleaned) if displayable else '',glossary_matches(cleaned,glossary),'final' if displayable else 'suppressed')
