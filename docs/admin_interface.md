# Admin Interface

This document describes the admin interface concept for the Church Live Translation System.

## Purpose

The admin interface is designed to help an operator monitor and manage the live translation workflow during a church service.

The public viewer is for attendees, while the admin interface is for the person responsible for starting, checking, and recovering the translation session if needed.

## Admin Goals

The admin interface should help the operator:

- Start or stop a translation session
- Monitor live translation status
- Confirm that the viewer display is updating
- Check recent translated segments
- Clear or reset a session when needed
- Identify issues without exposing technical details to attendees

## Main Admin Functions

| Function | Purpose |
|---|---|
| Session control | Start, stop, or reset a live translation session |
| Device/input status | Confirm that the correct audio input is selected |
| Live output monitoring | Preview what is being sent to the public viewer |
| Recent segment review | Check recent translation history |
| Clear session | Remove old content before a new service or test |
| Error awareness | Surface issues in a way the operator can understand |

## Session Control

The admin interface may include basic controls for managing a service session.

Example controls:

```text
Start Session
Stop Session
Clear Current Session
Restart Translation
```

These controls should be simple and difficult to misuse during a live service.

## Audio Input Awareness

A live translation system depends on correct audio input.

The admin interface may show information such as:

- Selected audio device
- Input status
- Whether audio appears to be detected
- Whether the speech-to-text process is active

The goal is not to overwhelm the operator with technical detail, but to make common setup problems easier to detect.

## Live Output Monitoring

The admin should be able to preview recent output before or while it appears on the public viewer.

Useful monitoring areas include:

- Latest speech-to-text result
- Latest cleaned source text
- Latest translated output
- Whether the public viewer has received recent updates

## Session Clearing

A clear session function is useful when preparing for a new service, test, or restart.

This may remove:

- Previous translated segments
- Temporary session memory
- Old viewer content
- Test output

This helps prevent old content from appearing during a new service.

## Error Handling

The admin interface should communicate errors in a practical way.

Instead of showing only technical exceptions, the interface should help the operator understand what action may be needed.

Example admin-facing messages:

```text
No audio input detected.
Translation is waiting for speech.
Viewer has not received updates recently.
Session memory was cleared.
```

## Public Viewer Separation

The admin interface should be separated from the public viewer.

Admin-only information should not appear on the attendee-facing page.

Admin-only information may include:

- Device settings
- Debug output
- Internal status messages
- Raw speech-to-text text
- Error logs
- Session reset controls

## Live-Service Design Priorities

Because the system may be used during an active worship service, the admin interface should prioritize:

- Fast recovery
- Simple controls
- Clear status indicators
- Low operator burden
- Minimal risk of accidental disruption
- Predictable behavior after restart or refresh

## Example Admin Workflow

```text
Open admin page
      ↓
Confirm audio input
      ↓
Start session
      ↓
Monitor live output
      ↓
Confirm viewer updates
      ↓
Clear session after service
      ↓
Review logs for improvement
```

## Portfolio Note

This document is a generalized and sanitized admin interface concept for portfolio purposes.

It does not include real admin URLs, private church infrastructure, production credentials, device identifiers, actual service logs, or personal information.
