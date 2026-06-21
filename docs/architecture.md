# 系统架构

```text
桌面状态采集端
  -> ActivityWatch / 前台窗口 / 键鼠 / AFK / 系统音频
  -> /desktop-context
  -> Context Normalizer
  -> Opportunity Detector
  -> Attention Policy
  -> Delivery Planner
  -> 机器人表情 / 动作 / 字幕 / 语音
```

```text
机器人音频
  -> VAD / STT / Transcript Guard
  -> Conversation Orchestrator
     -> Command Router
     -> Fast Chat
     -> Hermes Deep Agent
     -> Memory Service
  -> Response Normalizer
  -> TTS
  -> 机器人
```

## 责任边界

- 本地端：采集真实桌面状态，不承担自主 Agent 规划。
- 云端 Agent Brain：主动机会、注意力风控和表达方式判断。
- Hermes：复杂上下文、人格设定和反思建议。
- Memory Service：对话与主动交互共享的分层记忆。
- 硬件：执行表情、动作、字幕和语音。
