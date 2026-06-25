# 决策流与状态机

这份文档补充作品集首页中的 demo 流程、策略决策树和交互状态机，用来说明机器人不是“有提醒就语音播报”，而是先做风险判断，再选择表达强度。

## 三个 MVP 场景 demo

| 场景 | 输入信号 | 判断重点 | 策略输出 | 机器人表现 | 风险边界 |
| --- | --- | --- | --- | --- | --- |
| 会议勿扰 | 会议应用在前台、系统音频/麦克风活跃、持续低键盘输入 | 用户正在同步沟通，语音插入风险高 | `quiet` 或 `subtle` | 静默记录，必要时轻微表情 | 禁止普通主动语音 |
| 深度专注 | 工作应用在前台、持续输入、窗口切换少、专注时长增加 | 提醒价值可能存在，但中断成本高 | `subtitle`，冷却中降级为 `quiet` | 只显示短字幕，不抢占语音 | 同类提醒受冷却和每日预算限制 |
| 离席返回 | AFK 后恢复键鼠输入、桌面状态重新活跃 | 用户可能需要恢复上下文 | `subtle` 或 `subtitle` | 表情/轻动作，必要时给短提示 | 短离开不语音，信号不足不猜测 |

## 策略决策树

```text
收到主动机会
  -> 机器人是否可用？
      否 -> quiet，只记录原因
      是 -> 关键信号是否可用？
          否 -> quiet，标记 signal_unavailable
          是 -> 是否处于会议或高敏任务？
              是 -> quiet/subtle，禁止 speak
              否 -> 当前是否处于冷却或预算用尽？
                  是 -> 降级一级或 quiet
                  否 -> 计算任务敏感度、状态置信度、提醒价值
                      低价值或低置信 -> quiet/subtle
                      中价值且中置信 -> subtitle
                      高价值且高置信 -> speak，但仍受场景硬边界限制
```

## 交互状态机

```text
Idle
  -> Context Sensed
  -> Opportunity Candidate
  -> Attention Check
      -> Suppressed
          -> Log Reason
          -> Cooldown
          -> Idle
      -> Delivery Planned
          -> quiet / subtle / subtitle / speak
          -> User Response Observed
          -> Feedback Logged
          -> Cooldown
          -> Idle
```

## 触发与压制原因字典

| 字段 | 示例 | 用途 |
| --- | --- | --- |
| `scene` | `meeting_focus`、`deep_work`、`return_from_afk` | 记录当前场景 |
| `opportunity` | `break_reminder`、`resume_context`、`message_digest` | 记录主动机会 |
| `confidence` | `0.78` | 记录状态置信度 |
| `delivery_tier` | `quiet`、`subtle`、`subtitle`、`speak` | 记录最终表达强度 |
| `suppress_reason` | `meeting_active`、`cooldown`、`robot_offline` | 记录为什么不打扰 |
| `fallback_reason` | `signal_unavailable`、`hardware_unavailable` | 记录降级原因 |

## 策略配置样例

以下是脱敏后的策略配置格式示例，用于说明策略口径。它不是原始线上配置。

```json
{
  "scene": "meeting_focus",
  "hard_rules": [
    "no_speak_when_meeting_active",
    "downgrade_when_signal_unavailable"
  ],
  "signals": ["foreground_app", "audio_active", "keyboard_activity", "afk_state"],
  "delivery_budget": {
    "speak_per_day": 3,
    "subtitle_cooldown_minutes": 20,
    "subtle_cooldown_minutes": 10
  },
  "default_delivery": "quiet"
}
```

## 与 Agent 的关系

当前策略采用“规则策略优先，Agent 辅助判断”的方式：

- 规则策略负责会议禁语音、硬件离线只记录、信号不足自动降级等硬边界。
- Agent 用于复杂上下文摘要、偏好反思和策略建议，不绕过硬边界直接触发高打扰行为。
- 因此简历中应写“Agent 辅助判断框架”，不应写“自主 Agent 完成主动决策”。
