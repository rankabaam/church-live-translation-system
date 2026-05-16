# Workflow

This document describes the general workflow concept behind the Church Live Translation System.

## Purpose

The Church Live Translation System is designed to support live Korean-English sermon translation during church services.

The goal is to help attendees follow sermon content in real time through a public viewer interface while allowing an admin operator to monitor and manage the translation workflow.

## General Workflow

```text
Live Sermon Audio
        ↓
Speech-to-Text
        ↓
Text Cleanup / Correction
        ↓
Translation Processing
        ↓
Viewer Display
        ↓
Log Review
        ↓
Quality Improvement
```

## Step 1: Live Sermon Audio

The system begins with live spoken audio from a sermon, announcement, Scripture reading, or worship service segment.

The audio is used as input for speech-to-text processing.

## Step 2: Speech-to-Text

The spoken audio is converted into text using a speech-to-text process.

This step may include challenges such as:

- Long spoken sentences
- Pauses and breath timing
- Background noise
- Proper nouns
- Scripture references
- Korean-English mixed context

## Step 3: Text Cleanup and Correction

The raw speech-to-text output may require cleanup before translation.

This may include:

- Removing incomplete fragments
- Correcting common recognition errors
- Handling proper nouns through glossary support
- Improving sentence boundaries
- Preventing one-sided or incomplete output from reaching the public viewer

## Step 4: Translation Processing

The cleaned text is translated between Korean and English depending on the service context.

The translation process is designed to prioritize:

- Meaning over word-for-word translation
- Sermon context
- Readability for attendees
- Stability during live use
- Reduced confusion from partial or broken sentences

## Step 5: Viewer Display

The translated text is displayed through a public viewer interface.

The viewer interface is intended to be simple, readable, and comfortable for attendees to use during a live service.

Important viewer considerations include:

- Clear live text display
- Mobile browser compatibility
- Late-joining viewer support
- Minimal visual distraction
- Stable updates without unnecessary refreshes

## Step 6: Admin Monitoring

An admin interface may be used to monitor the live translation process.

Admin-side responsibilities may include:

- Starting or stopping a session
- Monitoring incoming text
- Checking translation behavior
- Clearing a session when needed
- Confirming that the public viewer is receiving updates

## Step 7: Log Review and Feedback

After a service, logs and translation output can be reviewed to identify improvement opportunities.

Review areas may include:

- Speech-to-text accuracy
- Sentence boundary quality
- Translation clarity
- Proper noun handling
- Viewer update behavior
- Cases where context was misunderstood

## Step 8: Quality Improvement

Feedback from live use can be converted into system improvements.

Possible improvement areas include:

- Glossary updates
- STT correction rules
- Better segmentation logic
- Improved viewer behavior
- More stable session memory
- Better handling of long sermon sentences

## Operational Value

This workflow demonstrates how a live translation system can support multilingual church environments by combining speech-to-text, translation processing, admin monitoring, and viewer display.

The system is not intended to replace human judgment or pastoral context. It is designed as a practical support tool for accessibility and understanding during live worship services.

## Privacy and Data Handling

This repository uses generalized documentation and fictional sample structures only.

No real sermon audio, private church data, production credentials, API keys, real service logs, or personal information are included.
