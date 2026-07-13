# Moqi System Architecture

## Three Product Surfaces

| Surface | Independent form | Responsibility |
| --- | --- | --- |
| Moqi Robot | ESP32-S3 desktop robot | Expression, gaze, motion, captions, voice, and continuous presence |
| Moqi for Windows | Tray app and control center | Local sensing, privacy, rhythm timeline, understanding review, pairing, and diagnostics |
| Moqi Cloud | Intelligent service and operations console | Authentication, signal fusion, visual understanding, proactive policy, memory, and device orchestration |

## End-to-End Flow

```text
Foreground app / desensitized title / dwell time / input rhythm / AFK / device state
  -> local SQLite timeline
  -> authenticated desktop context
  -> optional temporary active-window visual understanding
  -> proactive policy and memory retrieval
  -> compatible robot command(presence_mode, expression, motion, display_text, source)
  -> robot expression / gaze / caption / motion / voice
  -> robot feedback and user response
  -> memory confirm / correction / decay / deletion
```

## Local Data Lifecycle

- Raw activity segments: 7 days by default.
- Daily semantic summaries: 90 days by default.
- Stable preferences and rhythm memories: confidence and time-decay managed.
- ActivityWatch: optional enhancement source.
- Screenshots: active-window only after consent, held in memory, never written to disk.

Visual requests stop when Windows is locked, the user is AFK, a meeting device is active, or the foreground app is sensitive or excluded. A failed or unavailable vision request falls back to metadata understanding.

## Cloud Interfaces

| Method | Path | Purpose |
| --- | --- | --- |
| POST | `/api/v1/pair/claim` | Exchange a one-time pairing code for an installation credential |
| POST | `/api/v1/desktop/context` | Submit desensitized rhythm and semantic context |
| POST | `/api/v1/vision/understand` | Temporarily analyze an active-window image |
| GET | `/api/v1/companion/status` | Read local, cloud, robot, presence, and understanding state |
| GET/PUT | `/api/v1/preferences` | Manage visual consent, quiet hours, and expression preferences |
| GET/PATCH/DELETE | `/api/v1/memories` | Review, correct, confirm, or delete memory |
| POST | `/api/v1/feedback` | Record accepted, ignored, corrected, or uncomfortable feedback |

The legacy `/desktop-context` and `/ws` paths remain during migration. New desktop and vision requests require a paired installation token; tokens are stored as hashes on the server.

## Robot Presence States

`offline`, `connecting`, `quiet_present`, `noticed`, `available`, `listening`, `thinking`, `speaking`, `do_not_disturb`, `recovering`

`quiet_present` uses screen-level micro-expression without random servo motion. Meeting and high-focus states remain still. Cloud presence states map to the robot's existing expression, caption, motion, and voice commands.

## Product Boundaries

- Local sensing collects rhythm, not raw keystroke content.
- Broad task descriptions and user-confirmed project names may enter conversation; window titles, file names, messages, and account data do not.
- Low-confidence understanding stays internal.
- User correction updates or deletes the corresponding memory.
- The hardware is a purchased robot kit adapted through firmware and system integration.
