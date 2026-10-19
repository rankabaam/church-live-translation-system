"""Offline multilingual demonstration, using only a small fictional phrasebook.

NOT a speech recognizer, NLLB model, online translation service or language pack.
Unknown sentences are explicitly reported as unsupported.
"""
from __future__ import annotations

import re
from typing import Any

LANGUAGES = (
    {"code": "en", "label": "English"},
    {"code": "es", "label": "Español (demo only)"},
)

EXAMPLES = {
    "오늘 말씀을 통해 하나님의 은혜를 기억합니다.": {
        "en": "Through today's message, we remember God's grace.",
        "es": "A través del mensaje de hoy, recordamos la gracia de Dios.",
    },
    "우리는 서로를 사랑해야 합니다.": {
        "en": "We should love one another.",
        "es": "Debemos amarnos unos a otros.",
    },
    "믿음으로 한 걸음 나아갑시다.": {
        "en": "Let us take one step forward in faith.",
        "es": "Demos un paso adelante con fe.",
    },
}

CORRECTIONS = {
    "하나님의 은에": "하나님의 은혜",
    "성경 말슴": "성경 말씀",
}


def clean_text(text: str) -> str:
    normalized = re.sub(r"\s+", " ", text).strip()
    for old, new in CORRECTIONS.items():
        normalized = normalized.replace(old, new)
    return normalized


def translate_sample(
    text: str,
    *,
    language: str,
    is_final: bool = True,
    confidence: float | None = None,
    previous_final: str | None = None,
) -> dict[str, Any]:
    """Show explicit guard decisions; confidence is supplied by caller, never guessed."""
    if language not in {"en", "es"}:
        raise ValueError("Unsupported demo target language")
    if confidence is not None and not 0 <= confidence <= 1:
        raise ValueError("Confidence must be between 0 and 1")
    cleaned = clean_text(text)
    flags = []
    if not is_final:
        flags.append("partial_segment")
    if len(cleaned) < 4:
        flags.append("too_short")
    if confidence is not None and confidence < 0.55:
        flags.append("low_supplied_confidence")
    if previous_final is not None and clean_text(previous_final) == cleaned:
        flags.append("duplicate_final")
    if flags:
        return {"status": "suppressed", "source": cleaned,
                "target_language": language, "translation": "",
                "flags": flags, "mode": "offline_phrasebook_demo"}
    translated = EXAMPLES.get(cleaned, {}).get(language)
    if translated is None:
        return {"status": "unavailable", "source": cleaned, "target_language": language,
                "translation": "", "flags": ["phrase_not_in_demo_dictionary"],
                "mode": "offline_phrasebook_demo"}
    return {"status": "ready", "source": cleaned, "target_language": language,
            "translation": translated, "flags": [], "mode": "offline_phrasebook_demo"}
