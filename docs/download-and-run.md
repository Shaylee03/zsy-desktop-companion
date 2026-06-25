# 下载、启动与连接机器人

这个项目提供的是一个可传递的 Windows 原型体验包。它不是商业安装器，也不会自动接管用户电脑；下载者需要主动配置自己的后端地址和机器人配对信息。

## 下载内容

体验包：[`zsy-desktop-agent-starter.zip`](../downloads/zsy-desktop-agent-starter.zip)

解压后包含：

- `agent.py`：本地桌面状态采集 Agent。
- `config.example.json`：配置模板。
- `Start-ZSY-Desktop-Agent.ps1`：启动开关。
- `Stop-ZSY-Desktop-Agent.ps1`：停止开关。
- `Create-Desktop-Shortcuts.ps1`：创建桌面启动/停止快捷方式。
- `README.md` / `DESIGN.md`：运行说明和边界说明。

## 最小运行条件

- Windows 10/11。
- Python 3.10+ 已加入 PATH。
- 一个可访问的后端接口：`POST /desktop-context`。
- 一台已经接入该后端的机器人。
- 可选：ActivityWatch，用于更丰富的应用使用时长和 AFK 信号。

## 第一次启动

在解压目录运行：

```powershell
Copy-Item .\config.example.json .\config.local.json
notepad .\config.local.json
powershell -ExecutionPolicy Bypass -File .\Start-ZSY-Desktop-Agent.ps1
```

`config.local.json` 中至少需要设置：

```json
{
  "backendDesktopContextUrl": "http://your-backend-host:8000/desktop-context",
  "debugToken": "",
  "postBackend": true,
  "agentPort": 8765
}
```

启动后会打开本地面板：

```text
http://127.0.0.1:8765
```

## 桌面开关

为非技术测试者创建桌面快捷方式：

```powershell
powershell -ExecutionPolicy Bypass -File .\Create-Desktop-Shortcuts.ps1
```

桌面会出现：

- `Start ZSY Desktop Agent`
- `Stop ZSY Desktop Agent`

## 它如何连接机器人

本地 Agent 只负责上报桌面状态，例如：

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

也就是说，大模型不直接控制语音打断。高打扰行为必须经过策略层约束。

## 隐私边界

- 默认不使用摄像头画面识别。
- 默认不读取聊天内容。
- 默认不上报原始按键内容，只统计输入节奏。
- `config.local.json` 可能包含个人后端地址或 token，不应提交到公开仓库。

这个体验包的价值不是证明它已经是成熟商品，而是让面试官或测试者看到：项目已经从“产品概念”推进到“可启动、可配置、可连接机器人”的原型形态。
