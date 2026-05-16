# Church Live Translation System

A live Korean-English sermon translation workflow concept for church services.

## Overview

This project documents a real-time church translation support system designed to help Korean-English worship environments display live translated sermon text for attendees.

The system concept focuses on speech-to-text input, translation processing, viewer display, admin control, and iterative quality improvement based on live-service feedback.

## Problem

In multilingual church services, attendees may need translation support during sermons, announcements, or Scripture readings.

Manual interpretation or delayed translation can make it difficult for some attendees to follow the message in real time.

## Solution

This project demonstrates a live translation workflow that:

- Captures spoken sermon audio
- Converts speech to text
- Processes Korean-English translation
- Displays translated text through a viewer interface
- Supports admin-side monitoring and control
- Uses feedback and logs to improve translation quality over time

## Sample Workflow

```text
Sermon Audio
      ↓
Speech-to-Text
      ↓
Text Cleanup / Correction
      ↓
Translation
      ↓
Viewer Display
      ↓
Feedback Review
      ↓
Improvement Patch
```

## Documentation

- [System Architecture](docs/system_architecture.md)
- [Workflow](docs/workflow.md)
- [Engineering Challenges](docs/engineering_challenges.md)
- [Translation Quality](docs/translation_quality.md)
- [Admin Interface](docs/admin_interface.md)
- [Viewer Interface](docs/viewer_interface.md)
- [Session Memory](docs/session_memory.md)
- [Website Integration](docs/website_integration.md)
