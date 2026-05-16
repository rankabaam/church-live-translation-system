# System Architecture

This document describes the general system architecture concept behind the Church Live Translation System.

## Purpose

The Church Live Translation System is designed to support live Korean-English sermon translation during church services.

The system connects audio input, speech-to-text processing, translation logic, admin monitoring, viewer display, and post-service feedback review into one workflow.

## High-Level Architecture

```text
Live Audio Input
        ↓
Speech-to-Text Layer
        ↓
Text Cleanup / Segmentation Layer
        ↓
Translation Layer
        ↓
Session Memory / State Layer
        ↓
Public Viewer Interface
        ↓
Feedback and Log Review
```

## Main Components

| Component | Purpose |
|---|---|
| Audio Input | Receives live sermon or service audio |
| Speech-to-Text Layer | Converts spoken audio into text |
| Cleanup / Segmentation Layer | Improves sentence boundaries and removes incomplete fragments |
| Translation Layer | Converts text between Korean and English |
| Session Memory Layer | Stores recent translated segments for viewer continuity |
| Admin Interface | Allows an operator to monitor and manage the live session |
| Public Viewer Interface | Displays translated text to attendees |
| Logging / Feedback Layer | Supports post-service review and quality improvement |

## Audio Input Layer

The audio input layer receives live spoken content from a sermon, announcement, Scripture reading, or worship service segment.

Important considerations include:

- Clear audio capture
- Background noise reduction
- Stable input device selection
- Long spoken sentence handling
- Mixed Korean-English context

## Speech-to-Text Layer

The speech-to-text layer converts spoken audio into raw text.

Common challenges include:

- Long sentence recognition
- Proper nouns
- Scripture names and references
- Speaker pauses
- Partial phrases
- Misheard words

## Cleanup and Segmentation Layer

Before translation, the raw text may need cleanup.

This layer may handle:

- Removing incomplete fragments
- Holding partial text until a better boundary is detected
- Correcting common recognition errors
- Applying glossary-based fixes
- Preventing unstable one-sided output from reaching the public viewer

## Translation Layer

The translation layer converts cleaned text into the target language.

The translation process should prioritize:

- Meaning and context
- Natural readability
- Sermon tone
- Consistent terminology
- Reduced confusion from fragmented input

## Session Memory Layer

The session memory layer stores recent translated segments so viewers can continue seeing useful context.

This is especially important when:

- A viewer joins mid-service
- A mobile browser refreshes
- The display reconnects
- The admin interface needs to preserve recent output

Example concept:

```text
Recent Translation Segments
        ↓
Stored Temporarily
        ↓
Served to Viewer on Load or Refresh
```

## Admin Interface

The admin interface supports live operation and monitoring.

Possible admin functions include:

- Start or stop a session
- Monitor current translation output
- Confirm viewer update status
- Clear the current session
- Review system state
- Apply glossary or correction updates

## Public Viewer Interface

The public viewer interface displays translated text to attendees.

Important viewer goals include:

- Clear readable text
- Mobile-friendly layout
- Stable updates
- Minimal distraction
- Support for late-joining viewers
- Suppression of incomplete or one-sided output

## Logging and Feedback Layer

Logs can be reviewed after each service to improve the system.

Review areas may include:

- Speech-to-text accuracy
- Translation clarity
- Boundary detection
- Proper noun handling
- Viewer update behavior
- Long sentence handling
- Cases where context was misunderstood

## Example Data Flow

```text
Pastor speaks
    ↓
Audio is captured
    ↓
Speech-to-text produces raw text
    ↓
Cleanup layer improves text boundaries
    ↓
Translation layer generates viewer text
    ↓
Session memory stores recent segments
    ↓
Viewer displays translated output
    ↓
Logs are reviewed after service
```

## Design Priorities

The system is designed around practical live-use needs:

- Reliability during service
- Readability for attendees
- Low operator burden
- Recoverability if something goes wrong
- Iterative improvement based on real feedback
- Clear separation between admin control and public viewer display

## Portfolio Note

This architecture document is a generalized and sanitized description for portfolio purposes.

It does not include real production credentials, private church infrastructure, actual service logs, real sermon audio, or personal information.
