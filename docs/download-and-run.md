# 本地采集端与连接链路

这份文档说明当前原型中“桌面状态 -> 后端策略 -> 机器人反馈”的连接方式。真实运行需要本地环境、后端地址和机器人硬件配对，公开仓库主要提供作品集展示、架构说明和原型链路材料。

## 本地结构

本地采集端结构包含：

- `agent.py`：本地桌面状态采集端。
- `config.example.json`：配置模板。
- `Start-ZSY-Desktop-Agent.ps1`：启动脚本。
- `Stop-ZSY-Desktop-Agent.ps1`：停止脚本。
- `Create-Desktop-Shortcuts.ps1`：桌面启动/停止快捷方式脚本。
- `README.md` / `DESIGN.md`：运行说明和边界说明。

## 最小运行条件

- Windows 10/11。
- Python 3.10+ 已加入 PATH。
- 一个可访问的后端接口：`POST /desktop-context`。
- 一台已经接入该后端的机器人。
- 可选：ActivityWatch，用于更丰富的应用使用时长和 AFK 信号。

## 连接流程

```text
本地采集端
  -> 读取前台窗口、键鼠活跃、AFK、系统音频和应用使用时长
  -> POST /desktop-context
  -> 后端判断会议、专注、离席、返回、疲劳等状态
  -> 策略层选择 quiet / subtle / subtitle / speak
  -> 机器人执行表情、轻动作、字幕或语音
  -> 用户接受、忽略、关闭、延后或纠正
  -> 反馈进入记忆和策略权重
```

## 配置边界

`config.local.json` 中至少需要设置：

```json
{
  "backendDesktopContextUrl": "http://your-backend-host:8000/desktop-context",
  "debugToken": "",
  "postBackend": true,
  "agentPort": 8765
}
```

默认后端地址应指向本地或使用者自己的后端，不应把桌面状态默认发送到私人服务器。`config.local.json` 可能包含个人后端地址或 token，不应提交到公开仓库。

## 它如何连接机器人

本地采集端只负责上报桌面状态，例如：

- 当前前台窗口。
- 键鼠活跃与 AFK。
- ActivityWatch 应用使用摘要。
- 系统音频、麦克风、摄像头占用。
- 当前可打扰性提示。

后端根据这些状态，再结合任务优先级、用户偏好、记忆和安全边界，决定是否让机器人执行：

- `quiet`：静默记录。
- `subtle`：表情、灯效或轻动作。
- `subtitle`：屏幕字幕或小卡片。
- `speak`：语音播报。

也就是说，生成式能力不直接控制语音打断。高打扰行为必须经过策略层约束。

## 隐私边界

- 默认不使用摄像头画面识别。
- 默认不读取聊天内容。
- 默认不上报原始按键内容，只统计输入节奏。
- 公开材料不包含服务器凭据、个人 token、真实桌面日志或用户记忆。

这条链路展示了项目从“产品概念”推进到“可解释、可验证、可连接机器人”的原型形态，但不等同于商业安装器或开箱即用软件。
