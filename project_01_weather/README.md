# 项目一：天气预报查询 CLI

## 🎯 大目标

写一个命令行工具，输入 `python weather.py Beijing`，终端打印未来 3 天的天气。

## 📋 学习步骤

| 步骤 | 任务 | 输出物 |
|------|------|--------|
| 1.1 | 用浏览器访问 `wttr.in/Beijing?format=j1`，看懂返回的 JSON 结构 | 手画 JSON 结构图 |
| 1.2 | 用 `requests.get()` 拿到 JSON，`print(r.json())` 看结果 | 终端能打印出完整 JSON |
| 1.3 | 用 `json()` 方法提取「城市名」「日期」「最高温」「最低温」「天气描述」 | 终端打印格式化天气文本 |
| 1.4 | 用 `sys.argv` 接收命令行参数（城市名），支持中文城市 | `python weather.py 上海` 能查询上海天气 |
| 1.5 | 加错误处理：网络不通、城市不存在 | 友好的错误提示，不崩溃 |

## 🧠 核心技能

- HTTP GET 请求：`requests.get()`
- 响应处理：`.json()` `.raise_for_status()`
- 命令行参数：`sys.argv`
- 错误处理：`try/except`
- JSON 数据提取：字典嵌套访问

## ✅ 完成标准

- [ ] `python weather.py Tokyo` 打印 3 天天气预报
- [ ] `python weather.py A` （不存在的城市）显示友好错误提示
- [ ] 断网后运行，显示"网络连接失败"而非 traceback
- [ ] 代码有完整的函数注释

## 💡 进行中的记录

在 `../notes/day_01.md` 中记录你的学习过程。
