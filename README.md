# 桌面 AI 伴侣机器人：低打扰主动交互原型

这是一个面向学习与办公桌面场景的 AI 产品原型。项目关注的核心问题不是“机器人能不能主动说话”，而是：

> 什么时候的主动介入是帮助，什么时候会变成打扰？

项目使用前台窗口、键鼠活跃、AFK、ActivityWatch 和系统音频等桌面信号，辅助判断用户状态；再基于可打扰性、任务敏感度、信号置信度和设备可用性，在静默、表情/动作、字幕和语音之间选择合适的交互强度。

## 快速查看

作品集页面：

`https://shaylee03.github.io/zsy-desktop-companion/`

本仓库是静态作品集页面，不需要构建流程。克隆后可直接打开 `index.html`，也可以用本地静态服务查看：

```bash
python -m http.server 8000
```

然后访问 `http://localhost:8000`。

## 已实现

- 本地桌面状态采集与云端上报。
- 桌面状态识别与主动交互机会判断。
- `quiet / subtle / subtitle / speak` 四级介入策略。
- 会议、忙碌、信号不足、硬件离线等降级边界。
- Hermes 复杂上下文、人格设定与分层记忆原型。
- fast/deep 对话路由与延迟观测。
- Prompt、记忆、阈值和主动决策可观测后台。

## 面试官验证路径

| 想验证的问题 | 建议查看 | 当前能证明什么 | 当前不能证明什么 |
| --- | --- | --- | --- |
| 这个项目解决的问题是否真实 | [产品案例](docs/case-study.md) | 问题定义、MVP 场景、产品取舍 | 尚未证明目标用户规模和商业价值 |
| HRI 策略是否清楚 | [HRI 策略矩阵](docs/hri-strategy.md)、[决策流与状态机](docs/decision-flow.md) | 四级介入、硬边界、策略流转 | 尚未证明策略在大样本用户中有效 |
| 架构是否能落地 | [系统架构](docs/architecture.md)、[证据地图](docs/evidence-map.md) | 感知、决策、表达、观测的模块边界 | 公开仓库不包含脱敏前运行时代码 |
| 指标是否可信 | [指标与验证](docs/validation.md)、[访谈与自测计划](docs/research-and-self-test.md) | 路由延迟小样本基线、待验证指标口径 | 尚未得到误打扰率和接受率结论 |
| 是否过度包装 | [隐私与实现边界](docs/privacy-and-limitations.md) | 明确哪些是已验证、原型、待验证 | 不能把待验证内容写成结果 |

## 公开证据与边界

- [产品案例](docs/case-study.md)
- [HRI 策略矩阵](docs/hri-strategy.md)
- [系统架构](docs/architecture.md)
- [决策流与状态机](docs/decision-flow.md)
- [证据地图](docs/evidence-map.md)
- [指标与验证](docs/validation.md)
- [访谈与自测计划](docs/research-and-self-test.md)
- [隐私与实现边界](docs/privacy-and-limitations.md)

## 公开说明

本仓库是脱敏后的产品作品集，不包含服务器凭据、API Key、原始桌面日志、用户记忆、Hermes 会话和硬件固件。页面中所有指标都标注样本量和适用边界。

因此，简历中应写成“设计”“构建原型”“建立观测口径”“规划验证指标”，不应写成“已显著降低误打扰率”或“已完成大规模验证”。
