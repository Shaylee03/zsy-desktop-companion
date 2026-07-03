# ZSY Desktop Companion

> **Live Portfolio:**
> [shaylee03.github.io/zsy-desktop-companion](https://shaylee03.github.io/zsy-desktop-companion/)
>
> The portfolio site opens in English by default and includes a Chinese language switch in the page header.

<details>
<summary><strong>中文版本</strong></summary>

## 项目概览

ZSY Desktop Companion 是一个主动式桌面 AI 陪伴机器人原型，面向长时间学习、办公、写作和查资料的人群。项目探索一个放在电脑旁边的机器人如何感知桌面状态、理解学习 / 工作节奏、主动陪伴、学习用户偏好，并通过表情、字幕、动作或语音进行低压力回应。

在线作品集：[shaylee03.github.io/zsy-desktop-companion](https://shaylee03.github.io/zsy-desktop-companion/)

### 项目看点

| 模块 | 说明 |
| --- | --- |
| 桌面状态感知 | 本地感知端采集前台窗口、键鼠活跃、AFK、系统音频、ActivityWatch 等非摄像头信号，形成桌面状态摘要。 |
| 主动陪伴策略 | 后端根据桌面状态、场景风险、偏好和机器人可用性，在 `quiet / subtle / subtitle / speak` 中选择反馈强度。 |
| 记忆进化 | 记录任务上下文、长期偏好、行为节奏和交互反馈，让机器人逐步调整出现时机和表达方式。 |
| 机器人化反馈 | 将策略结果落到表情屏、底部字幕、点头 / 摇头 / 转向等动作，让主动策略具备可感知的机器人表达。 |

### 系统链路

```text
本地桌面感知端
  -> 桌面状态摘要
  -> 云端主动策略
  -> quiet / subtle / subtitle / speak
  -> 机器人表情 / 字幕 / 动作 / 语音
  -> 用户响应
  -> 记忆与偏好更新
```

### 硬件说明

硬件部分基于 ESP32-S3N16R8-EMOJI 桌面机器人硬件与开源固件框架进行适配。项目贡献重点在于产品定义、系统整合、后端策略、本地桌面感知端、固件配置适配和硬件联调；底层硬件与开源固件遵循其原有来源和许可。

### 本地预览

```bash
python -m http.server 8000
```

打开：

```text
http://localhost:8000
```

</details>

<p align="center">
  <img src="assets/hero-robot-background.jpg" alt="ZSY Desktop Companion robot prototype" width="100%">
</p>

<p align="center">
  <strong>Active Desktop AI Companion Robot</strong>
</p>

<p align="center">
  A portfolio-ready open-source prototype for study, office, writing, and remote-work scenarios.
  It explores how a small robot beside the computer can sense desktop state, understand work rhythm,
  proactively accompany the user, learn preferences, and respond through expression, captions, motion, or voice.
</p>

<p align="center">
  <a href="https://shaylee03.github.io/zsy-desktop-companion/"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-online-0f766e"></a>
  <a href="docs/architecture.md"><img alt="Architecture" src="https://img.shields.io/badge/Docs-architecture-2563eb"></a>
  <img alt="Status" src="https://img.shields.io/badge/Status-prototype-f59e0b">
  <img alt="Hardware" src="https://img.shields.io/badge/Hardware-off--the--shelf%20robot-64748b">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-111827"></a>
</p>

## Demo Video

<video src="https://raw.githubusercontent.com/Shaylee03/zsy-desktop-companion/89d877ccb68acffeffbf1fec5e8901992dd4e0f9/assets/demo.mp4" controls width="100%"></video>

Live demo video is also embedded in the portfolio page.

If the video does not render in GitHub, open the live portfolio:
[shaylee03.github.io/zsy-desktop-companion/#demo](https://shaylee03.github.io/zsy-desktop-companion/#demo)

## Project Overview

ZSY Desktop Companion explores an active desktop AI companion robot for people who study, write, research, or work alone in front of a computer for long sessions.

The core product question is:

> Can an AI companion understand desktop rhythm, appear at the right moment, respond with the right level of presence, and become more personal through long-term feedback?

## Highlights

| Area | What it shows |
| --- | --- |
| Desktop Sensing | A local desktop sensing client collects foreground window, keyboard/mouse activity, AFK, system audio, ActivityWatch, and other non-camera signals to form a desktop state summary. |
| Proactive Strategy | The backend selects a feedback tier from `quiet / subtle / subtitle / speak` based on desktop state, scene risk, preference, cooldown, and robot availability. |
| Memory Evolution | Task context, long-term preference, behavior rhythm, and interaction feedback help the robot adjust when to appear and how to respond. |
| Embodied Feedback | Strategy output is expressed through the robot screen, bottom captions, nodding, shaking, turning, and voice feedback. |

Low interruption is treated as the interaction boundary for proactive companionship.

## AI Boundaries

Generative AI is used for understanding user requests, generating natural wording, summarizing desktop activity, and organizing feedback into memory candidates.

The policy layer controls whether the robot should intervene, which feedback tier to use, meeting voice suppression, low-confidence downgrade, cooldown, and user preferences. The model is not allowed to directly control high-interruption behavior.

Model selection prioritizes stable Chinese dialogue, acceptable latency, controllable cost, and behavior that can be constrained by explicit rules. Real-time queries such as weather use built-in routes instead of free-form guessing.

## System Flow

```text
Local Desktop Sensing
  -> desktop state summary
  -> cloud proactive strategy
  -> quiet / subtle / subtitle / speak
  -> robot expression / caption / motion / voice
  -> user response
  -> memory and preference update
```

## What Is Included

| Module | Status | Notes |
| --- | --- | --- |
| Portfolio website | Done | Static case-study page covering product positioning, system logic, memory mechanism, hardware integration, and validation. |
| Local sensing side | Prototype | Local desktop state collection and `/desktop-context` reporting path. |
| Cloud proactive strategy | Prototype | Feedback tier selection based on state, risk, preference, cooldown, and robot availability. |
| Memory mechanism | Prototype | Structured model for task context, preference, rhythm, and interaction feedback. |
| Robot hardware integration | Linked | Custom backend access, WebSocket commands, expression, caption, and motion feedback chain. |
| Validation notes | Documented | Rule replay, small-sample prototype validation, page usability, and local chain checks. |

## Hardware Note

The robot hardware is an off-the-shelf desktop robot kit purchased for this prototype. The hardware integration is based on an ESP32-S3N16R8-EMOJI robot and an open-source firmware framework.

The project contribution focuses on product definition, system integration, backend strategy, local desktop sensing, firmware configuration, and hardware debugging. The base hardware and firmware follow their original sources and licenses.

## Representative Scenarios

| Scenario | System reading | Robot response |
| --- | --- | --- |
| Long study session | Lower input, long idle stays, or more window switching | Quiet logging, subtle motion, or short captions when risk is low |
| Task interruption | The user leaves the original task after multi-window switching | Caption-based task clue recovery at an appropriate moment |
| Meeting mode | Meeting software, microphone/camera, or system audio occupancy | Silent or weak feedback with voice suppressed |
| Deep focus | Work app stays foreground, input is stable, switching is low | Defer ordinary proactive opportunities |
| Return to desk | Input resumes after AFK | Short caption to restore context before stronger feedback |

## Prototype Validation

Current validation focuses on whether the prototype chain and policy paths match the product design. The scope is rule replay and small-sample prototype checks.

| Metric | Fixed trigger | Personalized memory strategy | Change |
| --- | --- | --- | --- |
| High-interruption trigger rate in meeting/focus scenes | 41% | 15% | -63% |
| Proactive feedback acceptance rate | 42% | 55% | +31% |
| Task recovery time after returning to desk | 125s | 80s | -36% |
| User correction rate after memory recall | 25% | 19% | -24% |

Details:

- [Validation notes](docs/validation.md)
- [Small-sample prototype validation](docs/small-sample-validation.md)
- [Evidence map](docs/evidence-map.md)
- [Privacy and limitations](docs/privacy-and-limitations.md)

## Quick Preview

This repository currently ships a static portfolio page for prototype preview and case-study reading.

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Documentation

- [Case study](docs/case-study.md)
- [Architecture](docs/architecture.md)
- [Interaction strategy](docs/interaction-strategy.md)
- [Decision flow](docs/decision-flow.md)
- [Memory evolution](docs/memory-evolution.md)
- [Local sensing and run notes](docs/download-and-run.md)

## Repository Map

```text
.
├── index.html                 # public portfolio page
├── styles.css                 # visual design
├── assets/                    # images used by the page and README
├── docs/                      # case study, architecture, strategy, validation
├── validation/                # prototype validation scripts
└── downloads/                 # archived local starter material for prototype documentation
```

## Roadmap

- Add hardware setup photos and a clearer robot command reference.
- Extract a minimal local sensing example that can run without private configuration.
- Improve memory review/editing screens for safer long-term personalization.

## Contributing

This is a personal portfolio prototype, but issues and documentation suggestions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code and documentation in this repository are released under the [MIT License](LICENSE), unless otherwise noted. The purchased robot hardware, third-party firmware framework, and external dependencies follow their own licenses.
