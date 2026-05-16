# Website Integration

This document describes the website integration concept for the Church Live Translation System.

## Purpose

The Church Live Translation System can be connected to a church website so attendees can access live translated sermon text during a worship service.

The public viewer page can be linked through a church website, QR code, bulletin, or shared service link.

## Integration Goal

The goal of website integration is to make live translation easy for attendees to access without requiring app installation or technical setup.

A visitor should be able to:

1. Open the church website or scan a QR code
2. Click the live translation link
3. View recent translated sermon text
4. Continue receiving live updates during the service

## Basic Integration Concept

```text
Church Website
      ↓
Live Translation Link / Button
      ↓
Public Viewer Page
      ↓
Recent Session Memory
      ↓
Live Translation Updates
```

## Public Viewer Access

The public viewer should be accessible through a simple attendee-facing link.

Example access methods:

- Church website button
- QR code displayed on screen or printed material
- Worship guide link
- Direct browser link
- Mobile bookmark

## Example Website Link Concept

A church website could include a button such as:

```html
<a href="https://example.com/live-translation">
  Live Translation
</a>
```

This is only a placeholder example.  
The public repository should not include real production URLs or private routing details.

## QR Code Use Case

A QR code can help attendees access the translation page quickly from a phone.

Example flow:

```text
Attendee scans QR code
        ↓
Phone opens live translation page
        ↓
Recent translated segments load
        ↓
New translation updates continue
```

## Viewer Page Requirements

The viewer page should be designed for public access.

Important requirements include:

- Mobile-friendly layout
- No login required for attendees
- No admin controls visible
- No debug logs visible
- No private system information exposed
- Stable refresh behavior
- Recent session memory support

## Admin and Public Separation

The public website link should only point to the attendee viewer page.

It should not expose:

- Admin dashboard
- Device settings
- Server logs
- API keys
- Internal configuration
- Cloud tunnel details
- Debug endpoints
- Private church infrastructure

## Deployment Concept

A live translation system may use a deployment structure similar to this:

```text
Local Translation System
        ↓
Local Web Server
        ↓
Secure Public Access Layer
        ↓
Church Website Link
        ↓
Attendee Viewer
```

This repository describes the concept only.

It does not include real deployment credentials, tunnel tokens, DNS configuration, server addresses, or production URLs.

## Operational Considerations

Website integration should account for live-service reliability.

Important considerations include:

- Link should be easy to find before and during service
- Viewer page should remain stable if attendees refresh
- Public page should not expose admin tools
- Session memory should prevent a blank page for late joiners
- The admin should be able to clear old session content before a new service
- The page should work well on mobile browsers

## Example Attendee Experience

```text
Before sermon:
Attendee opens church website or scans QR code.

During sermon:
Live translated text appears on the viewer page.

Mid-service join:
Recent translated segments load first, then live updates continue.

After service:
The admin may clear the session before the next service.
```

## Portfolio Note

This document is a generalized and sanitized website integration concept for portfolio purposes.

It does not include real church URLs, production credentials, Cloudflare tunnel details, private infrastructure, real viewer analytics, or personal information.
