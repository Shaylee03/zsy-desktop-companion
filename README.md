# Moqi

> An active desktop AI companion robot that learns your work rhythm through everyday computer use.

<p align="center">
  <a href="https://shaylee03.github.io/zsy-desktop-companion/"><img alt="Open the Moqi product case study" src="https://img.shields.io/badge/Open%20Portfolio-Moqi-167d75?style=for-the-badge"></a>
  <a href="#demo"><img alt="Watch demo" src="https://img.shields.io/badge/Watch-Demo-20282d?style=for-the-badge"></a>
</p>

<p align="center">
  <img src="assets/hero-robot-background.jpg" alt="Moqi desktop companion robot prototype" width="100%">
</p>

Moqi is a personal AI product and HRI prototype for graduate students, writers, researchers, and office workers who spend long sessions in front of a computer. It connects a Windows sensing app, a cloud intelligence layer, and a physical desktop robot into one continuous companion experience.

The robot remains quietly present by default. Desktop rhythm and user feedback help it decide when an expression, glance, caption, motion, or voice response is appropriate. Over time, correctable memory lets the experience adapt to individual preferences.

中文版本：[项目概览](#中文项目概览)

## Product Entry

**Live product case study:** [shaylee03.github.io/zsy-desktop-companion](https://shaylee03.github.io/zsy-desktop-companion/)

The portfolio opens in English by default. Use the `中文` switch in the header for the Chinese version.

## Project Overview

| Product surface | Role |
| --- | --- |
| Moqi Robot | The companion itself: expression, gaze, motion, captions, and voice |
| Moqi for Windows | Desktop sensing, privacy controls, system status, understanding review, and device diagnostics |
| Moqi Cloud | Signal fusion, proactive policy, visual understanding, long-term memory, and device orchestration |

## Why I Built This

Long computer sessions contain a rhythm that ordinary chat interfaces rarely see: focused work, rapid task switching, meetings, thinking pauses, leaving the desk, and returning to an interrupted task. Moqi explores how a physical AI companion can understand those transitions and provide continuity without demanding attention.

## Core Features

- **Quiet presence:** the robot stays connected and uses low-frequency expressions without random servo motion.
- **Desktop rhythm:** foreground app, desensitized title, dwell time, keyboard/mouse rhythm, AFK, and device state are summarized locally.
- **Optional visual understanding:** after explicit consent, the active window can be analyzed at low detail; screenshots are held in memory only and are not written to disk.
- **Proactive policy:** scene risk, confidence, cooldowns, preferences, and robot availability determine the response level.
- **Correctable memory:** users can review, confirm, edit, or delete long-term understanding.
- **Embodied response:** cloud commands carry presence mode, expression, motion, caption, lifetime, and source while retaining the current robot WebSocket format.

## System Architecture

```text
Moqi for Windows
  -> local SQLite rhythm timeline
  -> desensitized context / optional temporary visual analysis
  -> Moqi Cloud policy and memory
  -> compatible robot command
  -> Moqi Robot expression / gaze / caption / motion / voice
  -> robot feedback and user response
  -> memory update or decay
```

The migration keeps the legacy `/desktop-context` and `/ws` paths compatible while the authenticated `/api/v1/*` desktop interfaces become the default product path.

## Moqi for Windows

The Windows product uses a system tray plus a dedicated control center. It starts at login as a packaged application and does not require users to open Codex, PowerShell, or a system Python environment.

The control center provides:

- Home: local, cloud, and robot health; current presence mode; latest safe understanding.
- Understanding: recent timeline, semantic summaries, and correctable memory.
- Privacy & Data: visual consent, excluded apps, retention, pause, and deletion.
- Device: pairing, connectivity, data path, and diagnostics.

Local raw activity segments are retained for 7 days by default; semantic summaries are retained for 90 days. ActivityWatch remains an optional enhancement rather than a runtime dependency.

## Backend Strategy

The backend combines deterministic policy with language-model capabilities. Product rules control intervention level, meeting suppression, low-confidence fallback, cooldowns, and device availability. Generative models support natural language, broad desktop understanding, and memory candidates inside those constraints.

Versioned interfaces include pairing, desktop context, visual understanding, companion status, preferences, memories, and feedback. Installation credentials are stored as hashes on the server.

## Hardware Integration

The physical prototype uses a purchased ESP32-S3N16R8-EMOJI robot kit and an open-source firmware framework. My contribution focuses on product definition, system integration, backend strategy, local sensing, firmware adaptation, and hardware debugging.

## Demo

<video src="https://raw.githubusercontent.com/Shaylee03/zsy-desktop-companion/89d877ccb68acffeffbf1fec5e8901992dd4e0f9/assets/demo.mp4" controls width="100%"></video>

If GitHub does not render the video, open the [portfolio demo section](https://shaylee03.github.io/zsy-desktop-companion/#demo).

## Validation

Current validation covers policy replay, authenticated API behavior, local retention, privacy gates, existing robot command compatibility, and end-to-end prototype checks. The evaluation scope is a personal prototype and small-sample usability testing, not a large-scale user study.

- [Validation notes](docs/validation.md)
- [Architecture](docs/architecture.md)
- [Interaction strategy](docs/interaction-strategy.md)
- [Privacy and limitations](docs/privacy-and-limitations.md)

## How to Run This Repository

This public repository contains the portfolio and project documentation. Preview it locally with:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

Runtime credentials, private logs, and deployment configuration are not part of this repository.

## Current Limitations

- Windows 10/11 is the first supported desktop platform.
- The current product model supports one active user installation and one physical robot at a time.
- Visual understanding depends on explicit consent and a configured compatible vision provider.
- Longer multi-week use and broader usability testing are still needed.

## Roadmap

- Complete the signed Windows installer and paired onboarding flow.
- Add real control-center and hardware screenshots to the case study.
- Run 3-5 participant reset-isolated usability sessions.
- Refine memory review, correction, confidence decay, and bad-case tooling.

## 中文项目概览

Moqi 是一个主动式桌面 AI 陪伴机器人原型。它通过 Windows 本地应用理解用户的桌面节奏，由云端完成信号融合、主动策略和长期记忆，再由实体机器人通过表情、视线、动作、字幕或语音自然回应。

三端产品形态分别是：

- **Moqi Robot**：陪伴主体，负责表情、视线、动作、字幕和语音。
- **Moqi for Windows**：负责桌面感知、隐私控制、理解展示、连接状态和设备诊断。
- **Moqi Cloud**：负责策略判断、视觉理解、长期记忆和设备调度。

项目重点是产品定义、三端体验设计、主动交互策略、本地感知、后端整合、固件适配与硬件联调。默认状态是安静共在；低打扰作为主动陪伴的产品边界，由场景风险、置信度、用户偏好和设备状态共同控制。

## License

Code and documentation in this repository are released under the [MIT License](LICENSE), unless otherwise noted. Third-party hardware, firmware, and dependencies follow their own licenses.
