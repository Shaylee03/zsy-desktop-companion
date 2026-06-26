# 决策流与状态机

## 核心流程

```text
桌面状态变化
  -> 归一化信号
  -> 判断用户状态与置信度
  -> 识别主动机会
  -> 检查会议、专注、信号质量、硬件状态、冷却、预算、偏好
  -> 选择 quiet / subtle / subtitle / speak
  -> 记录用户反馈
  -> 更新策略和记忆权重
```

## 六个场景样例

| 场景 | 证据 | 用户状态判断 | 输出等级 | 机器人行为 | 硬边界 |
| --- | --- | --- | --- | --- | --- |
| 会议勿扰 | 会议应用、麦克风/摄像头、系统音频、日历 | 同步沟通中断成本高 | `quiet` / `subtle` | 静默记录或安静表情 | 禁止普通主动语音 |
| 深度专注 | 工作应用持续前台、键盘稳定、切换少 | 用户正在高价值任务中 | `quiet` / `subtitle` | 延后或短字幕 | 同类提醒受冷却和预算限制 |
| 离席返回 | AFK 后恢复输入、离席前任务存在 | 用户可能需要恢复上下文 | `subtitle` | 简短摘要，不直接语音 | 短离开不语音 |
| 连续工作 / 疲劳 | 长工作时长、输入下降、切换增多、晚间 | 疲劳或低效率风险上升 | `subtle` / `subtitle` / `speak` | 轻动作、字幕，严重时语音 | 会议和专注优先压制 |
| 任务遗忘恢复 | 原任务中断、频繁切换、当前可打扰 | 可能忘记原任务线索 | `subtitle` | 恢复任务提示 | 新任务专注中不打断 |
| 低能量支持 | 输入速度下降、停留无输入、切换增多 | 可能进入低效率状态 | `subtle` / `subtitle` | 低压力任务拆分建议 | 不做情绪诊断 |

## 策略决策树

```text
主动机会出现
  -> 机器人是否在线？
      否 -> quiet，只记录，不假装执行
      是 -> 关键信号是否可用？
          否 -> quiet，标记 signal_unavailable
          是 -> 是否处于会议或高敏任务？
              是 -> quiet/subtle，禁止 speak
              否 -> 是否处于深度专注？
                  是 -> 普通提醒延后或 subtitle
                  否 -> 冷却、预算或用户偏好是否限制？
                      是 -> 降级一级或 quiet
                      否 -> 按价值和置信度选择：
                          低价值或低置信 -> quiet/subtle
                          中价值且中置信 -> subtitle
                          高价值且高置信 -> speak
```

## 交互状态机

```text
Idle
  -> Context Sensed
  -> User State Inferred
  -> Opportunity Candidate
  -> Attention Check
  -> Delivery Planned
  -> quiet / subtle / subtitle / speak
  -> User Response Logged
  -> Memory Updated
  -> Cooldown
```

## 触发与压制原因字典

| 字段 | 示例 | 用途 |
| --- | --- | --- |
| `rhythm_event` | `meeting_active`、`work_scattered`、`return_short` | 当前状态事件 |
| `confidence` | `0.82` | 状态判断置信度 |
| `interaction_tier` | `quiet`、`subtle`、`subtitle`、`speak` | 最终反馈强度 |
| `suppression_reason` | `meeting_active`、`robot_offline`、`scene_disabled` | 为什么不提醒 |
| `downgrade_reason` | `voice_busy_to_subtitle`、`cooldown_to_subtle` | 为什么降级 |
| `policy_budget` | voice/subtitle/motion remaining | 今日预算 |
| `generated_line` | `true` / `false` | 是否使用生成式主动话术 |

## 策略配置样例

```json
{
  "hard_rules": [
    "no_speak_when_meeting_active",
    "record_only_when_robot_offline",
    "downgrade_when_signal_unavailable"
  ],
  "budgets": {
    "speak_per_day": 3,
    "subtitle_per_day": 12,
    "motion_per_day": 30
  },
  "cooldowns": {
    "subtitle_cooldown_minutes": 20,
    "subtle_cooldown_minutes": 10
  },
  "default_delivery": "quiet"
}
```

## 与生成式能力的关系

- 生成式能力负责理解提醒内容、生成自然语言、总结离席期间发生了什么、压缩行为日志。
- 规则策略负责会议禁语音、硬件离线只记录、信号不足自动降级和高打扰行为边界。
- 记忆只提供偏好和权重，不直接绕过安全边界。
