# Engineering Challenges

This document summarizes the main engineering challenges encountered while building a live church translation system for Korean-English sermon support.

The project was not only about translating text. The more difficult problems involved real-time delivery, session continuity, viewer reliability, operator usability, and translation quality under live service conditions.

---

## 1. Real-Time Service Environment

### Problem

Church services are live events. The system has to work while people are actively watching the translation, which means failures are immediately visible.

Unlike an offline translation workflow, there is limited time to manually correct mistakes during the service.

### Design Response

The system was designed around a practical live workflow:

- Admin interface for controlling the live translation session
- Public viewer interface for congregation access
- Segment-based translation output
- Session memory for recent translation history
- Sample correction files for glossary and STT issues
- Web integration for church website access

### Trade-Off

The system prioritizes operational reliability and readability over perfect translation accuracy. In a live service environment, a slightly delayed but coherent translation is usually better than a fast but broken output.

---

## 2. Session Memory for Late Joiners

### Problem

Viewers may open the translation page after the sermon has already started. Without session memory, late joiners would only see new translations and miss the previous context.

This was especially important for mobile users and people joining mid-service.

### Design Response

The system includes a session memory concept that stores recent translation segments and makes them available to newly connected viewers.

This allows the viewer page to display recent translation history instead of starting from an empty screen.

### Trade-Off

Keeping too much history can make the viewer page cluttered, while keeping too little history reduces usefulness for late joiners.

The sample design focuses on recent relevant segments rather than a full permanent transcript.

### Result / Current Status

The repository includes sample session memory data to demonstrate how recent translation segments can be preserved and reloaded.

Relevant sample:

- `samples/session_memory_sample.json`

---

## 3. Long Sermon Sentence Segmentation

### Problem

Sermons often contain long spoken sentences. Speakers may pause briefly without actually finishing a thought.

If the system cuts every short pause into a separate translation segment, the translation can lose context and become awkward or incorrect.

### Design Response

The translation workflow was designed around segment handling instead of treating every speech fragment as final immediately.

The system concept supports:

- Holding incomplete segments
- Merging related speech fragments
- Avoiding premature finalization
- Reviewing segment boundaries after the service

### Trade-Off

Longer waiting can improve context but may delay the viewer output. Shorter waiting feels faster but may produce weaker translations.

The project balances these competing goals by treating segmentation as a quality-control problem, not just a timing problem.

---

## 4. STT Errors and Contextual Misrecognition

### Problem

Speech-to-text errors can cause major translation errors. Korean homophones and context-sensitive phrases are especially difficult.

For example, a phrase like “아내로” could be misheard or interpreted incorrectly if the surrounding context is weak.

Biblical names, sermon references, and proper nouns can also be mistranscribed.

### Design Response

The project includes sample correction workflows:

- Glossary CSV for known terms and proper nouns
- STT correction CSV for repeated speech recognition issues
- Translation quality review document for post-service analysis

### Trade-Off

Automatic correction must be used carefully. Overly aggressive correction rules can fix one phrase while breaking another valid phrase.

The correction workflow is therefore designed as a controlled support layer rather than a blind replacement system.

### Relevant Samples

- `samples/glossary_sample.csv`
- `samples/stt_corrections_sample.csv`
- `docs/translation_quality.md`

---

## 5. Public Viewer Output Filtering

### Problem

During live processing, the system may temporarily have incomplete output, partial Korean-only text, or unfinished translation segments.

Showing incomplete internal processing text to the public viewer can confuse users.

### Design Response

The public viewer concept separates internal processing state from public display output.

The viewer should only show usable translated segments, while incomplete or one-sided internal lines remain hidden from the public interface.

### Trade-Off

Filtering improves viewer clarity but requires the system to decide when a segment is ready for display.

This creates a design distinction between internal draft state and public final output.

---

## 6. Admin Interface Reliability

### Problem

The translation system needs to be operated during a live service, often by non-developer users or volunteers.

The admin interface must therefore be simple and predictable.

Operational issues include:

- Audio device selection
- Applying device changes after restart
- Starting or clearing a session
- Monitoring whether translation is actively running
- Recovering from unexpected service behavior

### Design Response

The admin interface was designed around practical controls rather than developer-only commands.

Important admin-side concepts include:

- Device selection
- Apply button for audio input changes
- Session reset / clear function
- Live status visibility
- Simple layout for Sunday operation

### Trade-Off

More controls can improve flexibility, but too many controls can make the interface confusing during a live service.

The admin UI prioritizes the most common operational actions.

### Relevant Sample

- `samples/admin_ui_sample.html`

---

## 7. Mobile Viewer Consistency

### Problem

The public viewer may be opened on mobile browsers, desktop browsers, or embedded church website pages.

In testing, mobile viewers can behave differently from desktop viewers, especially when refreshing, reconnecting, or loading previous segments.

### Design Response

The viewer interface was designed to support:

- Recent segment loading
- Clear waiting state
- Readable mobile layout
- Separation between public display and admin controls

### Trade-Off

A mobile-first viewer needs to remain simple. Complex controls or dense transcript layouts can reduce readability during worship service.

The viewer interface focuses on clean text presentation and minimal user action.

### Relevant Sample

- `samples/viewer_ui_sample.html`

---

## 8. Website Integration

### Problem

The translation viewer needs to be accessible from the church website, but the live translation system itself may run separately from the public website.

This creates integration challenges around routing, embedding, refresh behavior, and public access.

### Design Response

The project includes website integration documentation and a sample HTML integration file.

The integration concept allows the public viewer to be linked or embedded from the church website while keeping the translation system modular.

### Trade-Off

A direct website integration is convenient for users, but the translation backend must remain controllable and isolated enough for live operation.

### Relevant Files

- `docs/website_integration.md`
- `samples/website_integration_sample.html`

---

## 9. Translation Quality Review

### Problem

Live translation quality cannot be improved only by guessing. After-service review is needed to identify recurring problems.

Common review targets include:

- Incorrect STT recognition
- Poor sentence boundaries
- Proper noun errors
- Incomplete translations
- Overly literal translations
- Missing context from previous segments

### Design Response

The project includes a translation quality review process.

The goal is to evaluate translation results after the service and use those findings to improve glossary entries, STT correction rules, segmentation logic, and viewer behavior.

### Trade-Off

Manual review takes time, but it provides more reliable improvement than changing the system based on isolated examples.

### Relevant File

- `docs/translation_quality.md`

---

## 10. Privacy and Deployment Considerations

### Problem

A real church translation system may process sermon audio, generated captions, internal logs, and deployment settings.

These should not be exposed in a public portfolio repository.

### Design Response

This repository uses sample files instead of real service data.

The public version excludes:

- Real sermon audio
- Private church logs
- API keys
- Internal server configuration
- Sensitive congregation information

### Trade-Off

The public repository cannot show every implementation detail, but it can still demonstrate the architecture, workflow, and engineering decisions behind the system.

---

## Summary

The main engineering challenge was not simply producing translated text.

The project required designing a live operational system that could handle:

- Real-time translation flow
- Late-joining viewers
- Long spoken sermon segments
- STT and glossary correction
- Public viewer filtering
- Admin-side usability
- Mobile and website access
- Post-service quality review

This made the project closer to a practical live captioning and translation workflow than a simple translation script.
