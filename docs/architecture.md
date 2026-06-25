# 系统架构

## 总体链路

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

## 模块职责

| 模块 | 输入 | 输出 | 责任边界 | 可公开证据 |
| --- | --- | --- | --- | --- |
| Desktop Context Collector | ActivityWatch、前台窗口、键鼠、AFK、系统音频 | 桌面状态摘要 | 只采集状态信号，不读取消息正文和摄像头画面 | 字段说明、脱敏日志样例 |
| Context Normalizer | 多源桌面信号 | 标准化上下文 | 合并信号、标记 unavailable，不强行猜测 | 状态字段字典 |
| Opportunity Detector | 标准化上下文、候选提醒 | 主动机会候选 | 判断是否存在提醒机会，不决定最终表达强度 | 触发原因日志 |
| Attention Policy | 场景、任务敏感度、置信度、冷却预算 | allow、suppress、downgrade | 处理会议禁语音、冷却、硬件离线等硬边界 | 策略矩阵、决策树 |
| Delivery Planner | 策略结果、设备状态 | quiet/subtle/subtitle/speak | 将策略结果映射到机器人表达 | 四级反馈表 |
| Conversation Orchestrator | 用户语音/文本、上下文 | fast/deep 路由 | 区分确定性指令、轻量对话和复杂上下文 | 路由延迟日志 |
| Memory Service | 用户反馈、偏好、历史行为 | 记忆读取与写入 | 记录偏好和反馈，不把命中效果包装成已验证 | 记忆字段说明 |
| Observability | 决策过程、模型路由、输出等级 | 日志、看板指标 | 记录触发、压制、降级和延迟原因 | 指标字典、看板截图 |

## 桌面上下文字段示例

以下字段用于说明公开口径，不包含真实用户数据。

```json
{
  "timestamp": "2026-06-18T10:30:00+08:00",
  "foreground_app": "meeting_app",
  "activity_state": "active",
  "afk_seconds": 0,
  "audio_active": true,
  "keyboard_active": false,
  "confidence": 0.82,
  "unavailable_signals": []
}
```

## 主动策略输出字段示例

```json
{
  "scene": "meeting_focus",
  "opportunity": "break_reminder",
  "decision": "suppress",
  "delivery_tier": "quiet",
  "suppress_reason": "meeting_active",
  "fallback_reason": null,
  "should_write_memory": false
}
```

## 责任边界

- 本地端：采集真实桌面状态，不承担自主 Agent 规划。
- 云端 Agent Brain：主动机会、注意力风控和表达方式判断。
- Hermes：复杂上下文、人格设定和反思建议。
- Memory Service：对话与主动交互共享的分层记忆。
- 硬件：执行表情、动作、字幕和语音。

## 公开仓库说明

公开仓库保留产品逻辑、策略边界、字段口径和验证计划。涉及服务器凭据、API Key、原始桌面日志、用户记忆、Hermes 会话和硬件固件的内容不公开。

因此，本仓库可以支撑“构建产品原型、设计策略框架、建立观测口径”的简历表述，但不能单独支撑“完整开源工程可运行”或“已大规模验证”的表述。
