# Session Memory

This document describes the session memory concept for the Church Live Translation System.

## Purpose

Session memory is designed to preserve recent translated segments during a live church service.

This helps viewers who join late, refresh their browser, or reconnect during the service continue seeing useful recent context instead of starting from an empty screen.

## Problem

In a live translation environment, viewers may not all open the page at the same time.

Common situations include:

- A viewer joins after the sermon has already started
- A mobile browser refreshes unexpectedly
- A viewer loses connection and reconnects
- The public display page reloads
- The admin restarts part of the workflow

Without session memory, the viewer may only see new translations after they connect, which can make the page feel empty or broken.

## Solution

The system can store recent translated segments temporarily and serve them to viewers when the page loads or refreshes.

## Basic Concept

```text
New translated segment
        ↓
Stored in session memory
        ↓
Viewer opens or refreshes page
        ↓
Recent segments are loaded
        ↓
Live updates continue
```

## What Session Memory Stores

Session memory may store recent viewer-ready translation segments.

Example fields:

| Field | Purpose |
|---|---|
| `segment_id` | Unique identifier for the translated segment |
| `timestamp` | Time when the segment was created |
| `source_language` | Original language |
| `target_language` | Display language |
| `display_text` | Final viewer-ready translated text |
| `status` | Whether the segment is final, held, or suppressed |

## Example Segment

```json
{
  "segment_id": "SEG-001",
  "timestamp": "2026-05-15T11:03:12",
  "source_language": "ko",
  "target_language": "en",
  "display_text": "Through today's message, we want to remember God's grace again.",
  "status": "final"
}
```

## Retention Window

Session memory should keep enough recent content to help viewers understand context, without storing unnecessary long-term data.

Example retention options:

| Option | Description |
|---|---|
| Last 10 segments | Keeps a limited number of recent translations |
| Last 30 minutes | Keeps recent service context for late joiners |
| Current session only | Clears memory when the session ends |
| Manual clear | Allows admin to clear memory before a new service |

## Viewer Load Behavior

When a viewer opens the public page, the system may:

1. Load recent translated segments from session memory
2. Display them in order
3. Continue receiving new live updates
4. Avoid duplicating already displayed segments

Example:

```text
Viewer joins at 11:15
        ↓
System loads recent translated segments
        ↓
Viewer sees current sermon context
        ↓
New translations continue appearing live
```

## Refresh Behavior

If a mobile browser refreshes, the viewer should not lose all visible content.

Session memory helps restore recent translated text after refresh.

Example:

```text
Browser refresh
        ↓
Viewer reconnects
        ↓
Recent session memory is loaded
        ↓
Live updates resume
```

## Admin Clear Behavior

The admin may need to clear session memory before a new service, test, or restart.

Clearing session memory may remove:

- Previous service translations
- Test output
- Old viewer content
- Temporary held segments

This helps prevent content from one service appearing during another.

## Incomplete Output Handling

Session memory should normally store only viewer-ready content.

It should avoid storing or displaying:

- Raw speech-to-text fragments
- One-sided source text without translation
- Duplicate partial lines
- Debug messages
- Admin-only content
- Text that has been intentionally suppressed

## Design Considerations

Session memory should balance continuity and privacy.

Important considerations include:

- Keep only recent service context
- Avoid long-term storage of sermon transcripts unless intentionally archived
- Allow manual clearing
- Avoid exposing admin/debug information
- Prevent duplicate display after refresh
- Keep viewer behavior predictable

## Example Session Memory Flow

```text
Speech-to-text result
        ↓
Cleanup and segmentation
        ↓
Translation
        ↓
Viewer-ready segment
        ↓
Store in session memory
        ↓
Send to public viewer
        ↓
Reload from memory if viewer reconnects
```

## Operational Value

Session memory improves live-service usability by making the viewer experience more stable.

It supports:

- Late-joining attendees
- Mobile browser refresh recovery
- More consistent public display
- Lower admin burden
- Better continuity during live translation

## Portfolio Note

This document is a generalized and sanitized session memory concept for portfolio purposes.

It does not include real service logs, private church data, production credentials, viewer analytics, or personal information.
