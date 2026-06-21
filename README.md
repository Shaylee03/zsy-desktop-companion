# 桌面 AI 伴侣机器人：低打扰主动交互原型

这是一个面向学习与办公桌面场景的 AI 产品原型。项目关注的核心问题不是“机器人能不能主动说话”，而是：

> 什么时候的主动介入是帮助，什么时候会变成打扰？

项目使用前台窗口、键鼠活跃、AFK、ActivityWatch 和系统音频等桌面信号，辅助判断用户状态；再基于可打扰性、任务敏感度、信号置信度和设备可用性，在静默、表情/动作、字幕和语音之间选择合适的交互强度。

## 作品集

GitHub Pages 启用后，访问：

`https://shaylee03.github.io/zsy-desktop-companion/`

## 已实现

- 本地桌面状态采集与云端上报。
- 桌面状态识别与主动交互机会判断。
- `quiet / subtle / subtitle / speak` 四级介入策略。
- 会议、忙碌、信号不足、硬件离线等降级边界。
- Hermes 复杂上下文、人格设定与分层记忆原型。
- fast/deep 对话路由与延迟观测。
- Prompt、记忆、阈值和主动决策可观测后台。

## 证据与边界

- [产品案例](docs/case-study.md)
- [HRI 策略矩阵](docs/hri-strategy.md)
- [系统架构](docs/architecture.md)
- [指标与验证](docs/validation.md)
- [隐私与实现边界](docs/privacy-and-limitations.md)

## 公开说明

本仓库是脱敏后的产品作品集，不包含服务器凭据、API Key、原始桌面日志、用户记忆、Hermes 会话和硬件固件。页面中所有指标都标注样本量和适用边界。
