# 低打扰主动式桌面 AI 机器人

这是一个面向学习、办公、远程协作和知识工作场景的个人独立项目。项目关注的核心问题不是“机器人能不能主动提醒”，而是：

> AI 什么时候应该主动介入，什么时候应该延后，什么时候应该静默，什么时候才允许语音？

系统使用前台窗口、ActivityWatch、键鼠活跃、AFK、系统音频、会议设备状态和应用使用时长等非摄像头信号，辅助判断用户是否处在会议、深度专注、离席返回、任务切换、疲劳或空闲状态；再根据状态置信度、任务优先级、用户偏好和安全边界，在 `quiet / subtle / subtitle / speak` 四级反馈中选择最低可行打扰强度。

## 在线查看

作品集页面：

`https://shaylee03.github.io/zsy-desktop-companion/`

Windows 原型体验包：

[`downloads/zsy-desktop-agent-starter.zip`](downloads/zsy-desktop-agent-starter.zip)

下载后可复制 `config.example.json` 为 `config.local.json`，填入自有后端 `/desktop-context` 地址，再运行 `Start-ZSY-Desktop-Agent.ps1` 启动本地桌面采集端。详细说明见 [下载、启动与连接机器人](docs/download-and-run.md)。

## 项目亮点

- 把主动式桌面助手的核心问题从“更频繁提醒”转成“控制主动介入边界”。
- 覆盖会议勿扰、深度专注、离席返回、连续工作、任务恢复和低能量支持等桌面场景。
- 将机器人反馈拆成 `quiet / subtle / subtitle / speak` 四级，并在会议、专注、信号不足、硬件离线、冷却和预算约束下自动降级。
- 设计短期上下文、长期偏好、行为节奏和交互反馈四类记忆，用于持续调整提醒时机和反馈强度。
- 提供可下载的 Windows 启动包，让下载者可以在本机启动桌面采集端，并连接自有后端和机器人。

## 当前交付

| 模块 | 当前状态 | 可查看内容 |
| --- | --- | --- |
| 产品案例页 | 已上线 | `index.html` |
| 本地桌面采集端启动包 | 已打包 | `downloads/zsy-desktop-agent-starter.zip` |
| 系统架构与策略 | 已文档化 | [系统架构](docs/architecture.md)、[主动交互策略](docs/interaction-strategy.md)、[决策流](docs/decision-flow.md) |
| 个性化记忆机制 | 已文档化 | [记忆进化机制](docs/memory-evolution.md) |
| 原型验证记录 | 已完成当前版本验证 | [验证记录](docs/validation.md)、[2026-06-26 验证结果](docs/validation-results-2026-06-26.md)、[实现匹配核查](docs/implementation-audit-2026-06-26.md)、[证据地图](docs/evidence-map.md) |
| 隐私与边界 | 已说明 | [隐私与实现边界](docs/privacy-and-limitations.md) |

## 验证摘要

当前版本已完成以下检查：

- 后端策略回放：会议勿扰、专注保护、离席返回、任务恢复等低打扰边界测试通过。
- 页面可用性：桌面端和移动端截图检查通过，链接完整，无移动端横向溢出。
- 下载包：Starter Kit 可访问，PowerShell 启动/停止脚本解析通过，包内未包含服务器密码或个人配置。
- 云端烟测：后端服务重启成功，健康检查和桌面状态接口返回 200。

验证详情见 [验证记录](docs/validation.md)。

## 本地查看页面

本仓库是静态作品集页面，不需要构建流程。克隆后可直接打开 `index.html`，也可以用本地静态服务查看：

```bash
python -m http.server 8000
```

然后访问 `http://localhost:8000`。

## 公开边界

公开仓库不包含服务器凭据、API Key、原始桌面日志、真实用户记忆、Hermes 会话和硬件固件。页面中展示的是脱敏后的产品逻辑、策略边界、启动包、验证记录和实现说明。
