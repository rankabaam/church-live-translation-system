# Multilingual Caption Selection — Synthetic Preview

This add-on demonstrates a possible presentation layer for multilingual captions without claiming that a production Spanish model or local language pack has been installed.

## What is implemented in this public portfolio

- Browser-based English / Spanish **output choice** at `/language-demo`.
- POST `/api/language-demo` with `source_text`, `target_language`, `is_final`, and optional `confidence` / `previous_final`.
- Fixed demonstration phrasebook of **three** Korean example phrases.
- No translation generated for unknown phrases.
- Explicit filtering of partial fragments, short text, duplicate final sentences, and caller-supplied low-confidence input.
- Unit tests, without external services or model downloads.

## How to run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
python -m unittest discover -s tests -v
```

Then visit `http://127.0.0.1:8000/language-demo` and try changing the output language.

## Production boundary

A local operational translator has separately used Silero VAD, faster-whisper and CTranslate2/NLLB-type processing. **None of those private integrations are provided or represented as running in this public preview.** Spanish language support was discussed as a possible future enhancement; the fixed Spanish sentences here **do not** establish that an operational Spanish model has been installed or evaluated. Quality flags here are deterministic input validation, not ASR confidence estimates or real context understanding.

This repo contains no recordings, streaming audio, private transcripts, deployment settings, credentials, or model assets.
