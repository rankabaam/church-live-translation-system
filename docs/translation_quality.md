# Translation Quality Review

This document describes the translation quality review concept used in the Church Live Translation System.

## Purpose

The Church Live Translation System is designed to improve over time through post-service review.

Because live sermon translation involves speech recognition, sentence boundaries, context, proper nouns, and real-time display behavior, translation quality should be evaluated across the full pipeline rather than only the final translated sentence.

## Quality Review Areas

Translation quality can be reviewed in several areas:

| Area | Review Focus |
|---|---|
| Speech-to-Text Accuracy | Whether spoken words were captured correctly |
| Sentence Boundary Quality | Whether long sermon sentences were split at natural points |
| Translation Clarity | Whether the translated message was understandable |
| Context Preservation | Whether the sermon meaning was preserved across segments |
| Proper Noun Handling | Whether names, locations, Bible references, and special terms were handled correctly |
| Viewer Display Stability | Whether translated text appeared clearly and consistently |
| Incomplete Output Suppression | Whether partial or one-sided text was prevented from reaching the public viewer |

## Speech-to-Text Accuracy

Speech-to-text quality is reviewed before judging the translation itself.

A poor translation may be caused by incorrect source text rather than the translation engine.

Common STT issues include:

- Misheard names
- Incorrect Bible references
- Missing words
- Long sentence collapse
- Background noise interference
- Mixed Korean-English phrases
- Similar-sounding Korean words

## Sentence Boundary Quality

Sermons often include long spoken sentences that are difficult to translate clearly if they are cut too early or too late.

Boundary quality review focuses on whether the system created segments that were:

- Complete enough to translate
- Not too long for live viewing
- Not too fragmented
- Contextually meaningful
- Easy for attendees to read

## Translation Clarity

The translated output should be evaluated based on meaning, readability, and usefulness for live attendees.

Good live translation should be:

- Clear
- Natural
- Context-aware
- Faithful to the sermon message
- Easy to follow in real time

The goal is not always word-for-word translation. In a live sermon setting, preserving the intended meaning is usually more important.

## Proper Noun and Glossary Handling

Proper nouns can create repeated translation problems if they are not handled consistently.

Examples may include:

- Bible names
- Book titles
- Speaker names
- Missionary names
- Church-specific terms
- Theological terms
- Korean names or English names

A glossary or correction list can help the system handle these terms more consistently.

## Incomplete Output Suppression

The public viewer should avoid displaying unstable or incomplete output.

Examples of output that should usually be held or suppressed:

- One-sided source text without translation
- Broken sentence fragments
- Duplicate partial lines
- Raw STT text that has not been processed
- Text that is likely to be replaced immediately

This helps make the viewer experience more stable and less distracting.

## Viewer Display Review

Viewer quality is not only about translation accuracy.

The display experience also matters.

Viewer review may include:

- Text readability
- Mobile browser behavior
- Late-joining viewer experience
- Refresh behavior
- Update speed
- Whether old text remains available long enough
- Whether the display feels distracting during worship

## Example Review Rubric

| Score | Meaning |
|---|---|
| 5 | Clear, accurate, natural, and useful for live attendees |
| 4 | Mostly clear with minor wording or timing issues |
| 3 | Understandable but noticeably awkward or incomplete |
| 2 | Confusing, fragmented, or contextually weak |
| 1 | Incorrect, missing, or not useful for attendees |

## Example Feedback Format

```text
Segment ID:
Source STT:
Displayed Translation:
Issue Type:
Severity:
Suggested Fix:
Notes:
```

## Example Issue Types

```text
STT_ERROR
BOUNDARY_TOO_SHORT
BOUNDARY_TOO_LONG
PROPER_NOUN_ERROR
TRANSLATION_UNNATURAL
CONTEXT_LOSS
DUPLICATE_OUTPUT
INCOMPLETE_OUTPUT
VIEWER_DISPLAY_ISSUE
```

## Improvement Loop

The quality review process supports an iterative improvement loop.

```text
Live Service
      ↓
Translation Logs
      ↓
Quality Review
      ↓
Issue Classification
      ↓
Glossary / Correction / Logic Update
      ↓
Next Service Test
```

## Practical Improvement Areas

Review findings may lead to improvements such as:

- Adding glossary entries
- Adding STT correction rules
- Improving sentence segmentation logic
- Adjusting viewer display behavior
- Improving session memory behavior
- Refining translation prompts or post-processing
- Reducing incomplete or duplicated output

## Portfolio Note

This document describes a generalized quality review framework for portfolio purposes.

It does not include real sermon logs, private church data, personal information, production credentials, or actual service transcripts.
