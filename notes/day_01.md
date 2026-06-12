# 第一天学习记录

## 📅 日期

2026-06-13

## 🎯 今日目标

完成 **项目一：天气预报查询 CLI** 的步骤 1.1 - 1.3

## 📋 任务分解

### 1.1 理解 API 结构（20 分钟）

- [ ] 用浏览器访问 `https://wttr.in/Beijing?format=j1`
- [ ] 观察返回的 JSON 结构
- [ ] 手画 JSON 结构图，标出：城市、日期、天气字段

**你的笔记：**

```
JSON 结构：

```

### 1.2 用 requests 获取数据（20 分钟）

- [ ] 打开终端，输入 `python` 进入 Python 交互式模式
- [ ] 尝试：`import requests`
- [ ] 尝试：`r = requests.get("https://wttr.in/Beijing?format=j1", timeout=10)`
- [ ] 尝试：`print(r.json())` 看完整响应

**你的笔记：**

```
获取成功吗？

第一个返回字段是什么？

```

### 1.3 提取天气数据（30 分钟）

- [ ] 在 `project_01_weather/weather.py` 中实现 `format_forecast()` 函数
- [ ] 提取字段：城市名、日期、最高温、最低温、天气描述
- [ ] 运行测试：`python weather.py Beijing`

**你的笔记：**

```
实现思路：

遇到的问题：

```

## 🧠 今日学到的知识点

1. **requests 库基础**
   - `requests.get(url, timeout=10)` 发起 GET 请求
   - `.json()` 方法自动解析 JSON
   - `raise_for_status()` 检查 HTTP 状态码

2. **JSON 数据访问**
   - 嵌套字典：`data["key1"]["key2"]`
   - 列表访问：`data["items"][0]`

3. **命令行参数**
   - `sys.argv[0]` 是脚本名
   - `sys.argv[1]` 及之后是用户输入的参数

## 🐛 遇到的问题及解决方案

| 问题 | 解决方案 | 状态 |
|------|--------|------|
| 例：导入 requests 失败 | 运行 `pip install requests` | ✅ 已解决 |
|  |  |  |
|  |  |  |

## 📚 查阅的资源

- [ ] requests 官方文档：https://requests.readthedocs.io/
- [ ] JSON 格式理解
- [ ] Python 字典操作

## ✅ 今日成果

- [ ] 理解 wttr.in API 的 JSON 结构
- [ ] 可以用 `requests.get()` 获取网络数据
- [ ] 实现了 `format_forecast()` 函数
- [ ] `python weather.py Beijing` 能成功输出天气

## 💡 明天计划

完成 **项目一** 的剩余部分（1.4 - 1.5）：
- 实现命令行参数支持（`sys.argv`）
- 添加错误处理（网络错误、城市不存在）
