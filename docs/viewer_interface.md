# Viewer Interface

This document describes the public viewer interface concept for the Church Live Translation System.

## Purpose

The viewer interface is designed to display live translated sermon text to attendees during a church service.

The goal is to make translated content easy to read, stable during live use, and minimally distracting in a worship environment.

## Viewer Goals

The public viewer should be:

- Simple
- Readable
- Mobile-friendly
- Stable during live updates
- Comfortable for long viewing
- Clear for late-joining viewers
- Free from unnecessary admin controls or technical details

## Main Viewer Functions

| Function | Purpose |
|---|---|
| Live translation display | Shows translated sermon text in near real time |
| Recent segment history | Allows attendees to see recent context |
| Waiting state | Shows a calm message when no translation is available yet |
| Mobile support | Allows attendees to view translation on phones |
| Auto-update behavior | Updates text without requiring manual refresh |
| Session memory support | Helps viewers who join mid-service see recent content |

## Display Priorities

The viewer interface should prioritize readability over visual complexity.

Important design considerations include:

- Large enough text for mobile screens
- Clear spacing between translated segments
- Low visual clutter
- Calm color palette
- No distracting animations
- No unnecessary technical labels
- Good contrast for readability

## Waiting State

When no translated text is currently available, the viewer should show a simple waiting message.

Example:

```text
Waiting for translation...
```

The waiting state should be calm and not visually distracting.

It should disappear automatically when translated text becomes available.

## Live Text Display

Translated text should appear in a clean sequence.

Example concept:

```text
Through today's message, we want to remember God's grace again.

Even when we feel lost, God is still guiding us.

Just as God worked in Ruth's life, He also works in our lives.
```

The viewer should avoid showing:

- Raw STT-only text
- Incomplete translation fragments
- Duplicate partial lines
- Admin-only debugging information
- One-sided source text without translation

## Late-Joining Viewer Support

A viewer may open the translation page after the sermon has already started.

To support this, the system may provide recent translated segments when the page loads.

Example concept:

```text
Viewer opens page mid-service
        ↓
Recent translated segments are loaded
        ↓
New live segments continue updating
```

This helps attendees understand recent context without requiring the admin to restart the session.

## Mobile Browser Considerations

Many attendees may use mobile browsers.

Important mobile considerations include:

- Responsive layout
- No required app installation
- Comfortable text size
- Stable scrolling behavior
- Minimal need for manual refresh
- Compatibility with common mobile browsers

## Public vs Admin Separation

The public viewer should not expose admin controls.

The viewer should not show:

- Start or stop buttons
- Debug logs
- API status
- Internal system messages
- Device selection controls
- Raw pipeline data

The public viewer should focus only on attendee-facing translated content.

## Error and Empty States

The viewer should handle empty or temporary states gracefully.

Possible states include:

| State | Viewer Behavior |
|---|---|
| No session started | Show a simple waiting message |
| Translation temporarily paused | Keep recent text visible and show a calm waiting indicator |
| Browser refresh | Reload recent session memory if available |
| Connection issue | Avoid showing confusing technical errors to attendees |

## Design Philosophy

The viewer interface should feel like a support tool, not a performance or distraction.

In a worship setting, the interface should help attendees follow the message while staying visually quiet and respectful of the service environment.

## Portfolio Note

This document is a generalized and sanitized viewer interface concept for portfolio purposes.

It does not include real service URLs, private church information, production credentials, actual viewer logs, or personal information.
