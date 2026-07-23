# Church Live Translation System

A sanitized real-time Korean-English translation system for live worship services, designed around operational reliability, readable output, and low operator burden.

## Overview

The project combines live audio capture, speech-to-text, text cleanup, machine translation, session memory, an operator interface, and a mobile-friendly viewer. This public repository documents the architecture and engineering decisions without exposing production credentials, recordings, private logs, or organization-specific infrastructure.

## Technical Direction

- Python and FastAPI service architecture
- Streaming speech-to-text using a locally hosted model
- Local neural machine translation
- Voice activity detection and sentence-boundary handling
- Glossary-assisted correction for names, Scripture terms, and recurring vocabulary
- Admin and viewer interfaces with session continuity
- GPU acceleration where available
- Post-service log review and regression tracking

## Generalized Architecture

```text
Live audio input
      ↓
Voice activity detection
      ↓
Streaming speech-to-text
      ↓
Cleanup, segmentation, and glossary corrections
      ↓
Machine translation
      ↓
Session state and recent-message memory
      ↓
Admin monitoring + public viewer
      ↓
Post-service feedback and regression review
```

## Engineering Priorities

- Prevent incomplete fragments from reaching viewers
- Preserve enough recent context for late-joining or reconnecting users
- Keep the operator workflow simple during live services
- Recover cleanly from audio, browser, or connection interruptions
- Improve terminology through controlled glossary and correction files
- Separate production data from public portfolio examples

## Documentation

- [System Architecture](docs/system_architecture.md)
- [Workflow](docs/workflow.md)
- [Engineering Challenges](docs/engineering_challenges.md)
- [Translation Quality](docs/translation_quality.md)
- [Admin Interface](docs/admin_interface.md)
- [Viewer Interface](docs/viewer_interface.md)
- [Session Memory](docs/session_memory.md)
- [Website Integration](docs/website_integration.md)

## Public Repository Scope

The included scripts and interfaces are simplified demonstrations. They do not contain real audio, service transcripts, production server addresses, credentials, private logs, or organization-specific configuration.

## Current Portfolio Direction

Future public-safe updates may include a more representative FastAPI demo, synthetic streaming input, configurable glossary loading, mock WebSocket updates, and automated checks for sentence suppression and session recovery.
