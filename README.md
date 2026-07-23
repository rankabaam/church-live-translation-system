# Church Live Translation System

A sanitized, runnable FastAPI and WebSocket demonstration of a Korean–English live-translation workflow designed around operational reliability, readable output, and low operator burden.

## Runnable Demo

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The browser demo lets an operator submit fictional Korean segments, mark them final or partial, and watch viewer session updates through WebSocket messages.

## Public Demo Architecture

```text
Synthetic source text
        ↓
Whitespace cleanup + correction rules
        ↓
Glossary matching
        ↓
Model-adapter interface
        ↓
Final/partial suppression decision
        ↓
Bounded session memory
        ↓
FastAPI REST endpoints + WebSocket broadcast
        ↓
Mobile-friendly browser viewer
```

The included `DemoTranslator` is deterministic and does not call a production speech-recognition or translation model.

## What the Project Demonstrates

- FastAPI REST and WebSocket service structure
- Health, processing, session, and clear endpoints
- Suppression of partial fragments
- Glossary-assisted terminology visibility
- Bounded recent-segment memory for late joiners
- Model-independent pipeline design
- Synthetic operator/viewer browser workflow
- Unit-tested correction, suppression, translation, and memory behavior

## Repository Contents

| Path | Description |
|---|---|
| `app/main.py` | FastAPI app, REST endpoints, WebSocket manager, and browser demo |
| `app/pipeline.py` | Cleanup, glossary, translation-adapter, and memory logic |
| `data/glossary_sample.json` | Fictional public glossary |
| `tests/test_pipeline.py` | Regression tests |
| `scripts/sample_translation_pipeline.py` | Command-line demonstration |
| `docs/` | Architecture and integration notes |
| `requirements.txt` | Demo dependencies |

## API Summary

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/health` | Service and mode check |
| `GET` | `/api/segments` | Current viewer-ready memory |
| `POST` | `/api/process` | Process a synthetic final or partial segment |
| `POST` | `/api/session/clear` | Clear the demo session |
| WebSocket | `/ws` | Receive snapshots and live updates |

## Validation

```bash
python -m unittest discover -s tests
python -m py_compile app/pipeline.py app/main.py
```

## Production Boundary

The operational system uses local speech recognition, neural machine translation, voice activity detection, glossary files, GPU acceleration, live audio, and service-specific controls. Those integrations are not published here.

This repository contains no recordings, transcripts, production model paths, server addresses, credentials, private logs, or organization-specific network configuration.
