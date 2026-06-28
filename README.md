# ZSY Desktop Companion

<p align="center">
  <img src="assets/hero-robot-background.jpg" alt="ZSY Desktop Companion robot prototype" width="100%">
</p>

<p align="center">
  <strong>主动式桌面 AI 陪伴机器人 / Active Desktop AI Companion Robot</strong>
</p>

<p align="center">
  A portfolio-ready open-source prototype for study, office and remote-work scenarios.
  <br>
  面向研究生与办公人群，探索一个放在电脑旁边的机器人如何感知桌面状态、主动陪伴、学习偏好，并用表情、字幕、动作或语音低压力地回应用户。
</p>

<p align="center">
  <a href="https://shaylee03.github.io/zsy-desktop-companion/"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-online-0f766e"></a>
  <a href="docs/architecture.md"><img alt="Architecture" src="https://img.shields.io/badge/Docs-architecture-2563eb"></a>
  <img alt="Status" src="https://img.shields.io/badge/Status-prototype-f59e0b">
  <img alt="Hardware" src="https://img.shields.io/badge/Hardware-off--the--shelf%20robot-64748b">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-111827"></a>
</p>

## Why / 项目初衷

People who study or work alone in front of a computer do not just need another chatbot or timer. They need a small desktop companion that understands rhythm: when to appear, when to stay quiet, and how to become more personal over time.

这个项目关注的不是“再做一个提醒工具”，而是：

> 长时间坐在电脑前学习或工作时，AI 能不能像一个懂节奏的桌面伙伴一样，在合适的时候主动出现，用合适的方式提供低压力陪伴，并随着使用逐步理解用户习惯？

## Highlights / 项目看点

| Area | What it shows |
| --- | --- |
| Desktop Sensing / 桌面状态感知 | 本地感知端采集前台窗口、键鼠活跃、AFK、系统音频、ActivityWatch 等非摄像头信号，形成桌面状态摘要。 |
| Proactive Strategy / 主动陪伴策略 | 后端根据桌面状态、场景风险、偏好和机器人可用性，在 `quiet / subtle / subtitle / speak` 中选择反馈强度。 |
| Memory Evolution / 记忆进化 | 记录任务上下文、长期偏好、行为节奏和交互反馈，让机器人逐步调整出现时机和表达方式。 |
| Embodied Feedback / 机器人化反馈 | 将策略结果落到表情屏、底部字幕、点头 / 摇头 / 转向等动作，而不是只停留在聊天窗口。 |

低打扰不是项目主卖点，而是主动陪伴必须遵守的 interaction boundary。

## System Flow / 系统链路

```text
Local Desktop Sensing
  -> desktop state summary
  -> cloud proactive strategy
  -> quiet / subtle / subtitle / speak
  -> robot expression / caption / motion / voice
  -> user response
  -> memory and preference update
```

## What Is Included / 当前仓库内容

| Module | Status | Notes |
| --- | --- | --- |
| Portfolio website | Done | 静态作品集页面，展示项目定位、系统逻辑、记忆机制、硬件联调和验证方式。 |
| Local sensing side | Prototype | 本地桌面状态采集与 `/desktop-context` 上报链路说明。 |
| Cloud proactive strategy | Prototype | 根据状态、风险、偏好、冷却和机器人可用性选择反馈强度。 |
| Memory mechanism | Prototype | 任务上下文、偏好、行为节奏、交互反馈的结构化说明和验证口径。 |
| Robot hardware integration | Linked | 自有后端接入、WebSocket 指令、表情 / 字幕 / 动作反馈链路已跑通。 |
| Validation notes | Documented | 规则回放、小样本路径验证、页面可用性和本地链路检查。 |

## Hardware Note / 硬件说明

The robot hardware is an off-the-shelf desktop robot kit purchased for this prototype. It is not hand-built from raw components.

硬件部分基于 ESP32-S3N16R8-EMOJI 桌面机器人硬件与开源固件框架进行适配。项目贡献重点在于产品定义、系统整合、后端策略、本地桌面感知端、固件配置适配和硬件联调，不把底层硬件或开源固件包装成从零原创。

## Representative Scenarios / 代表场景

| Scenario | System reading | Robot response |
| --- | --- | --- |
| Long study session / 长时间学习 | 输入下降、停留但推进慢、窗口切换增多 | 轻动作或短字幕，提供低压力节奏支持 |
| Task drift / 任务漂移 | 多窗口切换后离开原任务 | 在合适时机用字幕恢复任务线索 |
| Meeting mode / 会议中 | 会议软件、麦克风 / 摄像头或系统音频占用 | 禁止普通语音，静默或弱提示 |
| Deep focus / 深度专注 | 工作应用持续前台、输入稳定、切换少 | 延后普通主动机会 |
| Return to desk / 返回电脑 | AFK 后恢复输入 | 先用短字幕恢复状态，不直接语音打断 |

## Prototype Validation / 原型验证

当前验证目标是确认原型链路和规则路径是否符合产品设计，不包装成大规模商业化效果或正式用户实验。

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

## Quick Preview / 本地查看

This repository currently ships a static portfolio page. It does not provide a one-click consumer installer.

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Documentation / 文档入口

- [Case study](docs/case-study.md)
- [Architecture](docs/architecture.md)
- [Interaction strategy](docs/interaction-strategy.md)
- [Decision flow](docs/decision-flow.md)
- [Memory evolution](docs/memory-evolution.md)
- [Local sensing and run notes](docs/download-and-run.md)

## Repository Map / 目录结构

```text
.
├── index.html                 # public portfolio page
├── styles.css                 # visual design
├── assets/                    # images used by the page and README
├── docs/                      # case study, architecture, strategy, validation
├── validation/                # prototype validation scripts
└── downloads/                 # archived local starter material, not a consumer installer
```

## Roadmap / 后续计划

- Add a real demo video showing the local sensing side, backend policy and robot feedback chain.
- Add hardware setup photos and a clearer robot command reference.
- Extract a minimal local sensing example that can run without private configuration.
- Improve memory review/editing screens for safer long-term personalization.

## Contributing / 参与方式

This is a personal portfolio prototype, but issues and documentation suggestions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License / 许可

Code and documentation in this repository are released under the [MIT License](LICENSE), unless otherwise noted. The purchased robot hardware, third-party firmware framework and external dependencies follow their own licenses.
