"""
Church Live Translation System - Sample Translation Pipeline

This is a sanitized portfolio demo script.

It demonstrates the general structure of a live sermon translation workflow:
- receiving sample speech-to-text output
- applying simple STT correction rules
- checking glossary terms
- producing sample translated output
- storing viewer-ready segments in session memory

This script does not connect to real microphones, real translation APIs,
production servers, church infrastructure, or private service logs.
"""

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, List


STT_CORRECTIONS: Dict[str, str] = {
    "보아스가 룻을 안으로 받아들였다": "보아스가 룻을 아내로 받아들였다",
    "하나님의 은에": "하나님의 은혜",
    "배들레헴": "베들레헴",
    "성경 말슴": "성경 말씀",
    "예수 그리스도께서 우리를 구언하셨습니다": "예수 그리스도께서 우리를 구원하셨습니다",
}


GLOSSARY: Dict[str, str] = {
    "룻": "Ruth",
    "보아스": "Boaz",
    "나오미": "Naomi",
    "모압": "Moab",
    "베들레헴": "Bethlehem",
    "은혜": "grace",
    "구원": "salvation",
    "믿음": "faith",
    "소망": "hope",
    "회복": "restoration",
}


SAMPLE_TRANSLATIONS: Dict[str, str] = {
    "오늘 말씀을 통해 우리가 하나님의 은혜를 다시 기억하기 원합니다.":
        "Through today's message, we want to remember God's grace again.",

    "룻은 보아스를 통해 하나님의 보호하심을 경험하게 됩니다.":
        "Ruth experiences God's protection through Boaz.",

    "우리가 때로는 길을 잃은 것 같아도 하나님은 우리를 인도하고 계십니다.":
        "Even when we feel lost, God is still guiding us.",

    "하나님께서 룻의 삶 가운데 일하셨던 것처럼 우리의 삶 가운데도 일하십니다.":
        "Just as God worked in Ruth's life, He also works in our lives.",

    "보아스가 룻을 아내로 받아들였다":
        "Boaz accepted Ruth as his wife.",
}


@dataclass
class TranslationSegment:
    segment_id: str
    timestamp: str
    raw_stt: str
    cleaned_source: str
    displayed_translation: str
    glossary_matches: List[str]
    status: str


class SessionMemory:
    """Simple in-memory storage for recent viewer-ready translation segments."""

    def __init__(self, max_segments: int = 5) -> None:
        self.max_segments = max_segments
        self.recent_segments: List[TranslationSegment] = []

    def add_segment(self, segment: TranslationSegment) -> None:
        """Store a viewer-ready segment and keep only the most recent items."""
        if segment.status != "final":
            return

        self.recent_segments.append(segment)

        if len(self.recent_segments) > self.max_segments:
            self.recent_segments = self.recent_segments[-self.max_segments:]

    def get_recent_segments(self) -> List[dict]:
        """Return recent segments as dictionaries for viewer loading."""
        return [asdict(segment) for segment in self.recent_segments]


def apply_stt_corrections(raw_text: str) -> str:
    """Apply simple sample STT correction rules."""
    return STT_CORRECTIONS.get(raw_text, raw_text)


def find_glossary_matches(text: str) -> List[str]:
    """Find glossary terms that appear in the cleaned source text."""
    matches: List[str] = []

    for source_term, target_term in GLOSSARY.items():
        if source_term in text:
            matches.append(f"{source_term} -> {target_term}")

    return matches


def translate_sample_text(cleaned_source: str) -> str:
    """
    Return a sample translation.

    In a real system, this step could call a translation model,
    local model, or translation service. This demo uses fixed sample output.
    """
    return SAMPLE_TRANSLATIONS.get(
        cleaned_source,
        "[Sample translation not available for this fictional input.]",
    )


def should_display_to_viewer(cleaned_source: str, translation: str) -> bool:
    """
    Decide whether a segment should be displayed.

    This sample blocks empty or placeholder-only output.
    A real system may also suppress incomplete fragments or source-only text.
    """
    if not cleaned_source.strip():
        return False

    if translation.startswith("[Sample translation not available"):
        return False

    return True


def process_segment(segment_id: str, raw_stt: str) -> TranslationSegment:
    """Process one sample STT segment through the demo pipeline."""
    cleaned_source = apply_stt_corrections(raw_stt)
    glossary_matches = find_glossary_matches(cleaned_source)
    translated_text = translate_sample_text(cleaned_source)

    status = "final" if should_display_to_viewer(cleaned_source, translated_text) else "suppressed"

    return TranslationSegment(
        segment_id=segment_id,
        timestamp=datetime.now().isoformat(timespec="seconds"),
        raw_stt=raw_stt,
        cleaned_source=cleaned_source,
        displayed_translation=translated_text if status == "final" else "",
        glossary_matches=glossary_matches,
        status=status,
    )


def run_sample_pipeline() -> None:
    """Run a dry-run sample translation pipeline."""
    sample_inputs = [
        "오늘 말씀을 통해 우리가 하나님의 은혜를 다시 기억하기 원합니다.",
        "룻은 보아스를 통해 하나님의 보호하심을 경험하게 됩니다.",
        "우리가 때로는 길을 잃은 것 같아도 하나님은 우리를 인도하고 계십니다.",
        "보아스가 룻을 안으로 받아들였다",
        "하나님께서 룻의 삶 가운데 일하셨던 것처럼 우리의 삶 가운데도 일하십니다.",
    ]

    session_memory = SessionMemory(max_segments=5)

    print("Church Live Translation System - Sample Pipeline")
    print("------------------------------------------------")

    for index, raw_stt in enumerate(sample_inputs, start=1):
        segment_id = f"SEG-{index:03d}"
        segment = process_segment(segment_id, raw_stt)

        session_memory.add_segment(segment)

        print(f"\n{segment.segment_id}")
        print(f"Raw STT: {segment.raw_stt}")
        print(f"Cleaned Source: {segment.cleaned_source}")
        print(f"Glossary Matches: {segment.glossary_matches}")
        print(f"Displayed Translation: {segment.displayed_translation}")
        print(f"Status: {segment.status}")

    print("\nRecent Viewer-Ready Session Memory")
    print("----------------------------------")

    for segment in session_memory.get_recent_segments():
        print(f"{segment['segment_id']}: {segment['displayed_translation']}")


if __name__ == "__main__":
    run_sample_pipeline()
