# 系统架构

## 总体链路

```text
本地桌面 Agent
  -> 桌面状态感知
  -> 用户状态判断
  -> 主动介入决策
  -> 多模态反馈规划
  -> 机器人硬件执行
  -> 用户反馈回流
  -> 个性化记忆更新
```

## 六层架构

| 层级 | 输入 | 输出 | 职责 |
| --- | --- | --- | --- |
| 桌面状态感知层 | 前台窗口、ActivityWatch、键鼠、AFK、系统音频、会议设备、应用时长 | 原始桌面上下文 | 优先使用非摄像头、本地化、低隐私侵入信号 |
| 用户状态判断层 | 原始上下文、历史节奏、信号质量 | 会议、专注、离席、返回、疲劳、任务切换、可打扰等状态和置信度 | 把信号转成可解释状态 |
| 主动介入决策层 | 用户状态、任务优先级、偏好、机器人状态 | 是否提醒、是否延后、反馈等级、压制/降级原因 | 控制主动行为边界 |
| 多模态反馈层 | 策略结果、设备能力 | quiet/subtle/subtitle/speak | 将同一提醒映射为不同打扰强度 |
| 个性化记忆层 | 任务上下文、偏好、行为节奏、交互反馈 | 可调用偏好和策略权重 | 持续学习用户边界 |
| 观测与治理层 | 决策过程、路由、记忆、延迟、反馈 | 看板、日志、指标 | 复盘误提醒、错误记忆和强度不合适问题 |

## 模块职责

| 模块 | 作用 | 当前状态 |
| --- | --- | --- |
| Local Agent | 采集桌面状态并上报 `/desktop-context` | 已实现 |
| Windows Starter Kit | 提供配置模板、启动/停止脚本和桌面快捷方式创建脚本 | 已打包到公开仓库 |
| Desktop Rhythm Controller | rhythm event、冷却、预算、策略计划 | 已实现主体逻辑 |
| Proactive Brain | context normalizer、opportunity detector、attention policy、delivery planner | 已有模块化雏形 |
| Work Assistant | 专注、倒计时、提醒任务 | 已实现，与主动交互分层 |
| Memory Service | profile、procedural、rhythm、reflection 分层记忆 | 已实现基础存储和合并 |
| Admin Panel | Prompt、阈值、记忆、主动策略、路由延迟观测 | 已实现原型 |
| Firmware | 表情、动作、字幕、语音、WebSocket 执行 | 本地固件已支持字幕与动作指令 |

## 桌面上下文字段示例

```json
{
  "desktop_context": "coding",
  "current_app": "Code.exe",
  "current_title": "desktop_rhythm.py",
  "input_activity": {
    "keys_last_60s": 18,
    "mouse_clicks_last_60s": 2,
    "scroll_events_last_60s": 1,
    "idle_seconds": 4
  },
  "device_activity": {
    "mic_active": false,
    "camera_active": false,
    "audio_playing": false
  },
  "signal_quality": {
    "foreground": "available",
    "keyboard": "available",
    "mic": "available"
  }
}
```

## 主动策略输出字段示例

```json
{
  "rhythm_event": "work_scattered",
  "confidence": 0.82,
  "interaction_tier": "subtitle",
  "suppression_reason": "",
  "downgrade_reason": "cooldown_to_subtle",
  "decision_reason": "frequent_context_switches_5m",
  "policy_budget": {
    "voice": { "remaining": 3 },
    "subtitle": { "remaining": 8 },
    "motion": { "remaining": 24 }
  }
}
```

## 责任边界

- 本地 Agent 只采集和展示状态，不直接决定机器人是否说话。
- 状态判断层输出状态和置信度，不直接触发高打扰行为。
- Agent 可以生成话术和总结，但不能绕过会议禁语音、硬件离线、冷却和用户偏好。
- 长期记忆写入必须来自明确偏好、重复反馈或合并后的稳定结论。

## 公开仓库说明

公开仓库保留产品逻辑、策略边界、字段口径、验证计划和脱敏后的 Windows 本地 Agent starter。涉及服务器凭据、API Key、原始桌面日志、用户记忆、Hermes 会话和硬件固件的内容不公开。
