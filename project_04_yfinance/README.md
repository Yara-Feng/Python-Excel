# 项目四：精读 yfinance 源码

## 🎯 大目标

读懂 `ranaroussi/yfinance` 的核心代码，能画出数据流图，并自己实现一个「简化版」的股票数据获取工具。

## 📋 学习步骤

| 步骤 | 任务 | 输出物 |
|------|------|--------|
| 4.1 | `git clone` 仓库，只看目录结构，定位核心文件 | 手写「核心文件清单」 |
| 4.2 | 精读 `base.py` 中的 `TickerBase.history()` 方法 | 手写「history() 调用链」 |
| 4.3 | 追踪一次完整的 HTTP 请求（url → response → parse） | 截图或手写「请求流程图」 |
| 4.4 | 看 `utils.py` 中的数据清洗函数 | 列出 5 个 pandas 操作 |
| 4.5 | **自己写** `mini_yfinance.py`：只实现 `history()` 的简化版 | 一个能跑的简化版 |

## 🔍 为什么要读 yfinance？

yfinance 的核心逻辑：
```
用户调用 yf.Ticker("AAPL").history()
  → 内部用 requests 发 HTTP 到 Yahoo Finance API
  → 拿回 JSON
  → pandas 清洗、格式化
  → 返回 DataFrame
```

完美涵盖你学的三个核心库：**requests + pandas + json**

## 🧠 核心技能

- 阅读别人代码（追踪调用链、画流程图）
- HTTP API 逆向（从源码中理解 API 参数构造）
- pandas 数据清洗
- 模块化设计（入口层 → 逻辑层 → 工具层）
- 开源项目贡献准备

## ✅ 完成标准

- [ ] 能口述 `Ticker("AAPL").history()` 的完整调用链（3 分钟以内讲清楚）
- [ ] 画出数据流图：用户参数 → URL 构造 → HTTP 请求 → JSON → DataFrame
- [ ] `mini_yfinance.py` 能成功获取 AAPL 和 TSLA 的历史数据
- [ ] 对比你的输出和真实 yfinance 的输出，格式一致

## 📚 相关资源

- **yfinance GitHub**: https://github.com/ranaroussi/yfinance
- **yfinance 文档**: https://yfinance-python.org/
- **源码阅读笔记**: 记录在 `yfinance_notes.md`
