# 低打扰主动式桌面 AI 机器人

这是一个面向学习、办公、远程协作和知识工作场景的桌面 AI 机器人产品原型。项目关注的核心问题不是“机器人能不能主动提醒”，而是：

> AI 什么时候应该主动介入，什么时候应该延后，什么时候应该静默，什么时候才允许语音？

项目使用前台窗口、ActivityWatch、键鼠活跃、AFK、系统音频、会议设备状态和应用使用时长等非摄像头信号，辅助判断用户是否处在会议、深度专注、离席返回、任务切换、疲劳或空闲状态；再根据状态置信度、任务优先级、用户偏好和安全边界，在 `quiet / subtle / subtitle / speak` 四级反馈中选择最低可行打扰强度。

## 快速查看

作品集页面：

`https://shaylee03.github.io/zsy-desktop-companion/`

Windows 原型体验包：

[`downloads/zsy-desktop-agent-starter.zip`](downloads/zsy-desktop-agent-starter.zip)

下载后可复制 `config.example.json` 为 `config.local.json`，填入自己的后端 `/desktop-context` 地址，再运行 `Start-ZSY-Desktop-Agent.ps1` 启动本地桌面 Agent。详细说明见 [下载、启动与连接机器人](docs/download-and-run.md)。

本仓库是静态作品集页面，不需要构建流程。克隆后可直接打开 `index.html`，也可以用本地静态服务查看：

```bash
python -m http.server 8000
```

然后访问 `http://localhost:8000`。

## 当前项目进展

- 已搭建本地桌面 Agent，采集前台窗口、键鼠/AFK、ActivityWatch、系统音频、麦克风/摄像头占用等状态。
- 已接入云端后端 `/desktop-context`，将桌面状态输入主动策略层。
- 已实现 `quiet / subtle / subtitle / speak` 四级介入策略，并对会议、忙碌、信号不足、硬件离线、冷却、预算进行降级。
- 已有 rhythm event、主动机会判断、策略计划、生成式主动话术、反馈记录和自演化策略补丁雏形。
- 已接入 Hermes 复杂上下文、fast/deep 路由、分层记忆和管理后台。
- 已建立路由延迟、策略降级、记忆写入/跳过、主动反馈等观测口径。

## 面试官验证路径

| 想验证的问题 | 建议查看 | 当前能证明什么 | 当前不能证明什么 |
| --- | --- | --- | --- |
| 产品命题是否清楚 | [产品案例](docs/case-study.md) | 从“提醒”升级到“主动介入边界” | 尚未证明目标用户规模和商业价值 |
| 场景是否具体 | [HRI 策略矩阵](docs/hri-strategy.md)、[决策流与状态机](docs/decision-flow.md) | 会议、专注、离席返回、疲劳、任务恢复等策略 | 尚未证明所有场景已有真实样本 |
| 架构是否能落地 | [系统架构](docs/architecture.md)、[证据地图](docs/evidence-map.md) | 感知、状态、决策、反馈、记忆、观测的模块边界，以及可下载的本地 Agent starter | 公开仓库不包含云端凭据、原始日志和完整硬件固件 |
| 是否能被下载体验 | [下载、启动与连接机器人](docs/download-and-run.md) | 有 Windows 启动/停止脚本、配置模板和本地面板 | 仍需要测试者自己的后端和机器人配对信息 |
| 记忆机制是否专业 | [记忆进化机制](docs/memory-evolution.md) | 4 类记忆和记录、总结、合并、调用、更新、遗忘流程 | 尚未证明记忆命中显著改善体验 |
| 指标是否可信 | [指标与验证](docs/validation.md)、[访谈与自测计划](docs/research-and-self-test.md) | 路由延迟小样本基线、待验证指标口径 | 尚未得到误打扰率、接受率和记忆命中率结论 |
| 是否过度包装 | [隐私与实现边界](docs/privacy-and-limitations.md) | 明确哪些是已验证、原型、待验证 | 不能把待验证内容写成结果 |

## 公开证据与边界

- [产品案例](docs/case-study.md)
- [HRI 策略矩阵](docs/hri-strategy.md)
- [系统架构](docs/architecture.md)
- [决策流与状态机](docs/decision-flow.md)
- [记忆进化机制](docs/memory-evolution.md)
- [下载、启动与连接机器人](docs/download-and-run.md)
- [证据地图](docs/evidence-map.md)
- [指标与验证](docs/validation.md)
- [访谈与 3 天自测计划](docs/research-and-self-test.md)
- [隐私与实现边界](docs/privacy-and-limitations.md)

## 简历表达边界

推荐写法：

> 设计并构建低打扰主动式桌面 AI 机器人原型，围绕会议勿扰、深度专注、离席返回、连续工作提醒、任务恢复等场景，建立桌面状态感知、可打扰性判断、四级反馈策略和个性化记忆机制。

不建议写成：

- 已商业化产品。
- 已完成大规模用户验证。
- 已显著降低误打扰率。
- 机器人已经能准确理解全部用户状态。

公开仓库不包含服务器凭据、API Key、原始桌面日志、用户记忆、Hermes 会话和硬件固件。页面中所有指标都标注样本量和适用边界。
