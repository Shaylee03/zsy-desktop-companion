# Privacy and Limitations

## Local-First Controls

Moqi for Windows keeps a local SQLite rhythm timeline and exposes pause, visual consent, excluded apps, retention, and deletion controls in the product UI.

- Foreground titles are desensitized before cloud upload.
- Raw key content is never recorded; only activity counts and rhythm are used.
- Visual understanding is disabled until explicit consent.
- Visual capture is limited to the active window at a configurable interval.
- Locked screen, AFK, meetings, password managers, chat, banking, and excluded apps stop capture.
- Image bytes remain in memory during analysis and are not written to local or server storage.
- Cloud responses contain only task category, safe summary, sensitivity, confidence, and a constrained memory suggestion.

## Memory Controls

Users can inspect, correct, confirm, or delete memory. Desktop understanding may be referenced in conversation only when it is relevant and safe. The setting can be disabled independently of desktop sensing.

Default retention:

- Raw activity segments: 7 days.
- Semantic summaries: 90 days.
- Stable preferences: confidence and time-decay managed.

## Current Limitations

- Windows 10/11 is the first supported desktop platform.
- The current product model supports one active user installation and one robot at a time.
- Visual understanding requires a configured compatible provider and is subject to model uncertainty.
- The prototype still needs longer multi-week use and 3-5 reset-isolated usability sessions.
- Base robot hardware and upstream firmware are third-party components.

## Public Repository Scope

The public repository contains the product case study, architecture, interaction strategy, validation notes, and media. Runtime credentials, private logs, personal memory, and deployment secrets remain outside version control.
