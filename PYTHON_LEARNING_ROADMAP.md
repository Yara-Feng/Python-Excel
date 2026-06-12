# Python 实战学习路线图

> **适用对象**：基础 Python 水平（了解变量、循环、函数），「数据 + 网络 + 自动化」方向。
>
> **核心库**：`requests` `pandas` `os` `sys` `argparse` `pathlib` `json` `csv`
>
> **学习策略**：「抄 → 改 → 创」三步法，每个项目都有明确完成标准。

---

## 目录

1. [学习理念](#学习理念)
2. [项目一：天气预报查询 CLI](#项目一天气预报查询-cli)
3. [项目二：B站热榜抓取 → CSV](#项目二b站热榜抓取--csv)
4. [项目三：文件批量重命名 CLI](#项目三文件批量重命名-cli)
5. [项目四：精读 yfinance 源码](#项目四精读-yfinance-源码)
6. [技能树总览](#技能树总览)
7. [附录：资料索引](#附录资料索引)

---

## 学习理念

### 三个原则

| 原则 | 做法 | 反例 |
|------|------|------|
| **先跑通，再理解** | 代码抄完能运行就是胜利 | 纠结每一行语法，结果一行都没跑 |
| **一项目一技能** | 每个项目主练 1-2 个核心库 | 一个项目塞 5 个库，贪多嚼不烂 |
| **完成标准硬** | 每个步骤有明确的"输出物" | "我大概看懂了" |

### 每拿到一个新 API 的标准流程

```
1. 打开终端 →  import 库 → 调用函数 → print 返回值
2. 改参数 → 看输出变化
3. 写进 .py 文件 → 加错误处理 → 完成
```

**永远在终端里先试，不要直接在文件里写。**

---

## 项目一：天气预报查询 CLI

### 🎯 大目标

> 写一个命令行工具，输入 `python weather.py Beijing`，终端打印未来 3 天的天气。

### 📋 小目标拆解

| 步骤 | 任务 | 预计用时 | 输出物 |
|------|------|----------|--------|
| 1.1 | 用浏览器访问 `wttr.in/Beijing?format=j1`，看懂返回的 JSON 结构 | 20 分钟 | 手画 JSON 结构图（城市→日期→天气字段） |
| 1.2 | 用 `requests.get()` 拿到 JSON，`print(r.json())` 看结果 | 20 分钟 | 终端能打印出完整 JSON |
| 1.3 | 用 `json()` 方法提取「城市名」「日期」「最高温」「最低温」「天气描述」 | 30 分钟 | 终端打印出格式化的天气文本 |
| 1.4 | 用 `sys.argv` 接收命令行参数（城市名），支持中文城市 | 20 分钟 | `python weather.py 上海` 能查询上海天气 |
| 1.5 | 加错误处理：网络不通、城市不存在 | 20 分钟 | 提示友好的错误信息而非报错崩溃 |

### 🏗️ 核心代码骨架

```python
"""weather.py — 终端天气预报查询"""
import sys
import requests

def get_weather(city: str) -> dict:
    """调用 wttr.in API，返回原始 JSON 数据"""
    url = f"https://wttr.in/{city}?format=j1"
    r = requests.get(url, timeout=10)
    r.raise_for_status()  # 如果 HTTP 状态码不是 200，抛出异常
    return r.json()

def format_forecast(data: dict, days: int = 3) -> str:
    """从 JSON 中提取未来 N 天的天气，返回格式化字符串"""
    # TODO: 你的代码
    pass

def main():
    if len(sys.argv) < 2:
        print("用法：python weather.py <城市名>")
        sys.exit(1)
    city = sys.argv[1]
    try:
        data = get_weather(city)
        print(format_forecast(data))
    except requests.exceptions.ConnectionError:
        print("网络连接失败，请检查网络。")
    except requests.exceptions.HTTPError:
        print(f"查询失败：找不到城市「{city}」")

if __name__ == "__main__":
    main()
```

> **你的任务**：实现 `format_forecast()` 函数。提示——JSON 路径是：
> ```
> data["weather"][0]["astronomy"]  → 日出日落
> data["weather"][0]["hourly"]     → 逐小时数据
> data["weather"][0]["avgtempC"]   → 日均温（实际在 date 的字段里）
> ```

### 🧠 本项目主练技能

| 技能 | 库/知识点 | 深度 |
|------|-----------|------|
| HTTP GET 请求 | `requests.get()` | ⭐ 入门 |
| 响应处理 | `.json()` `.raise_for_status()` | ⭐ 入门 |
| 命令行参数 | `sys.argv` | ⭐ 入门 |
| 错误处理 | `try/except` | ⭐ 入门 |
| JSON 数据提取 | 字典嵌套访问 `data["key"]["subkey"]` | ⭐ 入门 |

### ✅ 完成标准（全部通过才算过）

- [ ] `python weather.py Tokyo` 打印 3 天天气预报
- [ ] `python weather.py A` （不存在的城市）显示友好错误提示
- [ ] 断网后运行，显示"网络连接失败"而非 traceback
- [ ] 代码有完整的函数注释（每个函数一句话说明干什么）

---

## 项目二：B站热榜抓取 → CSV

### 🎯 大目标

> 抓取 B 站热门视频列表，输出到 CSV 文件，包含：排名、标题、播放量、UP 主、视频链接。

### 📋 小目标拆解

| 步骤 | 任务 | 预计用时 | 输出物 |
|------|------|----------|--------|
| 2.1 | 浏览器访问 `https://api.bilibili.com/x/web-interface/popular` 看懂 JSON | 15 分钟 | 手写 JSON 结构树 |
| 2.2 | `requests.get()` 拿到数据，打印第一个视频的标题 | 20 分钟 | 终端输出一个视频标题 |
| 2.3 | `for` 循环遍历所有视频，用 `print` 逐条打印 | 15 分钟 | 终端列出 100 条视频 |
| 2.4 | 把数据整理成 `list[dict]`，用 `csv.DictWriter` 写入 CSV | 30 分钟 | 生成 `bilibili_hot.csv` |
| 2.5 | 用 `pandas` 读回 CSV，按播放量排序，打印 Top 10 | 20 分钟 | 终端输出播放量最高的 10 个视频 |
| 2.6 | 加命令行参数 `--count N` 控制抓取条数 | 20 分钟 | `python bilibili.py --count 20` |

### 🏗️ 核心代码骨架

```python
"""bilibili.py — B站热门视频抓取，输出 CSV"""
import sys
import csv
import requests
import pandas as pd  # 用于读回 CSV 做排序

API_URL = "https://api.bilibili.com/x/web-interface/popular"

def fetch_hot_videos() -> list[dict]:
    """抓取 B 站热门视频列表，返回清洗后的数据"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.bilibili.com/",
    }
    r = requests.get(API_URL, headers=headers, timeout=15)
    r.raise_for_status()
    data = r.json()
    # TODO: 从 data 中提取视频列表
    videos = data["data"]["list"]  # ← 关键：找到数据在哪里
    result = []
    for v in videos:
        result.append({
            "排名": len(result) + 1,
            "标题": v["title"],
            "播放量": v["stat"]["view"],
            "弹幕数": v["stat"]["danmaku"],
            "UP主": v["owner"]["name"],
            "链接": f"https://www.bilibili.com/video/{v['bvid']}",
        })
    return result

def save_to_csv(videos: list[dict], filename: str = "bilibili_hot.csv"):
    """将视频列表写入 CSV 文件"""
    # TODO: 用 csv.DictWriter 实现
    pass

def show_top(csv_file: str, n: int = 10):
    """用 pandas 读取 CSV，按播放量排序，打印 Top N"""
    df = pd.read_csv(csv_file)
    # TODO: 按播放量降序排列，打印前 N 行
    print(df.sort_values("播放量", ascending=False).head(n))

def main():
    print("正在抓取 B 站热门…")
    videos = fetch_hot_videos()
    print(f"获取到 {len(videos)} 条视频")
    save_to_csv(videos)
    print(f"已保存到 bilibili_hot.csv")
    show_top("bilibili_hot.csv")

if __name__ == "__main__":
    main()
```

### 🧠 本项目主练技能

| 技能 | 库/知识点 | 深度 |
|------|-----------|------|
| 带 Header 的 HTTP 请求 | `requests` + `headers` | ⭐⭐ 进阶 |
| 嵌套 JSON 数据提取 | `dict["key1"]["key2"]["key3"]` | ⭐⭐ 进阶 |
| CSV 写入 | `csv.DictWriter` | ⭐ 入门 |
| 数据处理 | `pandas.read_csv()` `sort_values()` `head()` | ⭐ 入门 |
| 列表推导 + 数据清洗 | `[x for x in ...]` | ⭐⭐ 进阶 |

### ✅ 完成标准

- [ ] 运行后生成 `bilibili_hot.csv`，可用 Excel 直接打开
- [ ] CSV 中包含 5 个字段（排名、标题、播放量、UP主、链接）
- [ ] 终端输出播放量 Top 10
- [ ] 程序运行时间 < 10 秒
- [ ] 网络不通时有友好提示

---

## 项目三：文件批量重命名 CLI

### 🎯 大目标

> 写一个终端工具，输入文件夹路径和规则，批量重命名文件。支持 `--dry-run` 预览模式（不实际修改）。

### 📋 小目标拆解

| 步骤 | 任务 | 预计用时 | 输出物 |
|------|------|----------|--------|
| 3.1 | 用 `pathlib.Path.iterdir()` 列出文件夹内所有文件 | 15 分钟 | 终端打印文件清单 |
| 3.2 | 实现「加前缀」规则：`python rename.py ./test --prefix "IMG_"` | 20 分钟 | 预览模式下看到新文件名 |
| 3.3 | 实现「按序号编号」规则：`python rename.py ./test --number` | 20 分钟 | `File.txt` → `001_File.txt` |
| 3.4 | 实现「替换文字」规则：`python rename.py ./test --replace "旧" "新"` | 20 分钟 | 名称中的文字被替换 |
| 3.5 | 实现 `--dry-run` 预览模式（默认开启，加 `--execute` 才真正改名） | 20 分钟 | 安全：默认只预览 |
| 3.6 | 用 `argparse` 重构命令行参数（取代手动解析 `sys.argv`） | 30 分钟 | 完整的 `--help` 输出 |

### 🏗️ 核心代码骨架

```python
"""rename.py — 批量文件重命名工具"""
import argparse
from pathlib import Path

def list_files(folder: Path) -> list[Path]:
    """返回文件夹内所有文件的路径列表（不含子目录）"""
    return [f for f in folder.iterdir() if f.is_file()]

def preview_rename(folder: Path, old_name: str, new_name: str) -> None:
    """打印重命名预览"""
    print(f"  {old_name}  →  {new_name}")

def execute_rename(folder: Path, old_name: str, new_name: str) -> None:
    """实际执行重命名"""
    (folder / old_name).rename(folder / new_name)
    print(f"  ✓ {old_name}  →  {new_name}")

def add_prefix(files: list[Path], prefix: str) -> list[tuple[str, str]]:
    """为所有文件加前缀"""
    # TODO: 返回 [(旧名, 新名), ...]
    return [(f.name, prefix + f.name) for f in files]

def replace_text(files: list[Path], old: str, new: str) -> list[tuple[str, str]]:
    """替换文件名中的文字"""
    # TODO
    pass

def number_files(files: list[Path]) -> list[tuple[str, str]]:
    """按顺序编号（保持原有扩展名）"""
    # TODO: 001_原名、002_原名...
    pass

def main():
    parser = argparse.ArgumentParser(description="批量文件重命名工具")
    parser.add_argument("folder", help="目标文件夹路径")
    parser.add_argument("--prefix", help="添加前缀，如 --prefix 'IMG_'")
    parser.add_argument("--replace", nargs=2, metavar=("OLD", "NEW"), help="替换文字")
    parser.add_argument("--number", action="store_true", help="按序号编号")
    parser.add_argument("--execute", action="store_true", help="实际执行（默认仅预览）")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.exists():
        print(f"错误：文件夹 '{args.folder}' 不存在")
        return

    files = list_files(folder)
    print(f"找到 {len(files)} 个文件\n")

    # TODO: 根据参数选择重命名规则
    # TODO: 遍历执行 preview_rename 或 execute_rename

if __name__ == "__main__":
    main()
```

### 🧠 本项目主练技能

| 技能 | 库/知识点 | 深度 |
|------|-----------|------|
| 命令行参数解析 | `argparse` | ⭐⭐ 进阶 |
| 文件系统操作 | `pathlib.Path` | ⭐⭐ 进阶 |
| 安全设计思维 | `--dry-run` 模式 | ⭐ 入门（但很重要） |
| 函数组合 | 多个规则函数复用同一个执行逻辑 | ⭐⭐ 进阶 |
| 字符串操作 | `.replace()` `f-string` | ⭐ 入门 |

### ✅ 完成标准

- [ ] `python rename.py --help` 输出完整的帮助信息
- [ ] `python rename.py ./test --prefix "IMG_"` 预览重命名结果
- [ ] `python rename.py ./test --number --execute` 真正改名
- [ ] `python rename.py ./test --replace "旧" "新"` 替换文字
- [ ] 默认 `--dry-run` 模式，不加 `--execute` 不修改任何文件
- [ ] 处理文件名冲突（已存在同名文件时不覆盖，给出警告）

---

## 项目四：精读 yfinance 源码

### 🎯 大目标

> 读懂 `ranaroussi/yfinance` 的核心代码，能画出数据流图，并自己实现一个「简化版」的股票数据获取工具。

### 🔍 为什么要读 yfinance？

```
yfinance 的核心逻辑：
  用户调用 yf.Ticker("AAPL").history()
  → 内部用 requests 发 HTTP 到 Yahoo Finance API
  → 拿回 JSON
  → pandas 清洗、格式化
  → 返回 DataFrame

完美涵盖你学的三个核心库：requests + pandas + json
```

### 📋 小目标拆解

| 步骤 | 任务 | 预计用时 | 输出物 |
|------|------|----------|--------|
| 4.1 | `git clone` 仓库，只看目录结构，定位核心文件 | 15 分钟 | 手写「核心文件清单」 |
| 4.2 | 精读 `base.py` 中的 `TickerBase.history()` 方法 | 45 分钟 | 手写「history() 调用链」 |
| 4.3 | 追踪一次完整的 HTTP 请求（url → response → parse） | 30 分钟 | 截图或手写「请求流程图」 |
| 4.4 | 看 `utils.py` 中的数据清洗函数（空值处理、列重命名） | 30 分钟 | 列出 5 个 pandas 操作 |
| 4.5 | **自己写** `mini_yfinance.py`：只实现 `history()` 的简化版 | 60 分钟 | 一个能跑的简化版 |

### 🏗️ 精读指南

#### 第一步：定位核心文件

```bash
git clone https://github.com/ranaroussi/yfinance.git
cd yfinance
ls yfinance/
# 你会看到：base.py, ticker.py, utils.py, multi.py ...
```

重点读这三个文件：

| 文件 | 作用 | 先读哪个 |
|------|------|----------|
| `yfinance/ticker.py` | 用户入口：`Ticker("AAPL")` | 🥇 先读 |
| `yfinance/base.py` | 核心逻辑：`history()` 方法的实现 | 🥈 精读 |
| `yfinance/utils.py` | 工具函数：数据清洗、格式转换 | 🥉 选读 |

#### 第二步：追踪一次调用链

```python
# 1. ticker.py — 用户入口
class Ticker:
    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self._base = TickerBase(...)  # 核心实现在这里

    def history(self, period="1mo", ...):
        return self._base.history(period=period, ...)

# 2. base.py — 核心逻辑（你重点读这个）
class TickerBase:
    def history(self, period="1mo", ...):
        # a) 构造 URL
        # b) requests.get(url)
        # c) 解析 JSON → DataFrame
        # d) 数据清洗（时区、列名、空值）
        # e) 返回 DataFrame
        return df
```

#### 第三步：自己写简化版

```python
"""mini_yfinance.py — 极简版 Yahoo Finance 数据获取"""
import requests
import pandas as pd

def get_stock_history(ticker: str, period: str = "1mo") -> pd.DataFrame:
    """
    获取美股历史行情。
    ticker: 股票代码，如 "AAPL"
    period: 时间范围，如 "1mo", "3mo", "1y"
    """
    # TODO: 参考 yfinance 源码，实现核心逻辑
    # 1. 构造请求 URL
    # 2. requests.get()
    # 3. 解析 JSON
    # 4. 转为 DataFrame 并清洗
    pass

# 测试
df = get_stock_history("AAPL")
print(df.head(10))
```

### 🧠 本项目主练技能

| 技能 | 说明 | 深度 |
|------|------|------|
| 阅读别人代码 | 追踪调用链、画流程图 | ⭐⭐⭐ 核心能力 |
| HTTP API 逆向 | 从源码中理解 API 参数构造 | ⭐⭐⭐ 核心能力 |
| pandas 数据清洗 | 空值、时区、列重命名 | ⭐⭐ 进阶 |
| 模块化设计 | 理解「入口层 → 逻辑层 → 工具层」的分层 | ⭐⭐⭐ 核心能力 |
| 开源项目贡献准备 | clone → 读 → 改 → 跑测试 | ⭐⭐ 进阶 |

### ✅ 完成标准

- [ ] 能口述 `Ticker("AAPL").history()` 的完整调用链（3 分钟以内讲清楚）
- [ ] 画出数据流图：用户参数 → URL 构造 → HTTP 请求 → JSON → DataFrame
- [ ] `mini_yfinance.py` 能成功获取 AAPL 和 TSLA 的历史数据
- [ ] 对比你的输出和真实 yfinance 的输出，格式一致

---

## 技能树总览

学完四个项目后，你应该具备以下能力：

### 库掌握程度

```
requests         ████████░░  熟练：GET/POST、Headers、超时、异常处理
pandas           ██████░░░░  会用：read_csv、DataFrame 基本操作、排序/筛选
argparse         ██████░░░░  会用：位置参数、可选参数、--help
os / pathlib     ██████░░░░  会用：文件遍历、重命名、路径拼接
json             ████████░░  熟练：load/dump、嵌套解析
csv              ██████░░░░  会用：DictReader/DictWriter
sys              ████░░░░░░  了解：argv、exit
```

### 通用能力

| 能力 | 通过哪个项目练的 |
|------|-----------------|
| 「抄→改→创」三步学习法 | 全部四个项目 |
| 看懂陌生 JSON 结构 | 项目一、二 |
| 阅读并复现开源项目核心逻辑 | 项目四 |
| 写一个完整的 CLI 工具（含帮助文档） | 项目三 |
| 用 try/except 做防御性编程 | 全部四个项目 |
| 用 print + type() 调试 | 全部四个项目 |
| 查官方文档而非 CSDN | 附录指引 |

---

## 附录：资料索引

### 📖 官方文档（首选，永远先看这个）

| 库 | 官方文档 |
|----|---------|
| requests | https://requests.readthedocs.io/en/latest/ |
| pandas | https://pandas.pydata.org/docs/ |
| argparse | https://docs.python.org/zh-cn/3/library/argparse.html |
| pathlib | https://docs.python.org/zh-cn/3/library/pathlib.html |
| csv | https://docs.python.org/zh-cn/3/library/csv.html |
| json | https://docs.python.org/zh-cn/3/library/json.html |
| sys | https://docs.python.org/zh-cn/3/library/sys.html |

### 🎥 推荐教程（当官方文档太干时看）

| 主题 | 资源 | 说明 |
|------|------|------|
| requests 快速入门 | Real Python: "Python's Requests Library (Guide)" | 最推荐，英文但示例清晰 |
| pandas 10 分钟入门 | pandas 官网的 "10 Minutes to pandas" | 官方出品，必读 |
| argparse 教程 | Real Python: "Build Command-Line Interfaces With argparse" | 项目三直接参考 |
| B 站 API 分析 | 搜索 "B站 API 热门视频" → SocialSisterYi/bilibili-API-collect | 非官方 API 文档合集 |

### 🧩 知识点速查

| 你不熟的知识点 | 搜索关键词 | 看哪个结果 |
|---------------|-----------|-----------|
| `if __name__ == "__main__"` 是什么意思 | `python if __name__ main explained` | Real Python 或 StackOverflow |
| `dict.get()` 和 `dict[key]` 的区别 | `python dict get vs bracket` | GeeksforGeeks |
| `try/except` 怎么用 | `python try except tutorial` | Python 官方教程 |
| `f-string` 格式化数字 | `python f-string format number` | Real Python |
| `list[dict]` 是什么意思 | `python type hints list dict` | Python 官方 typing 文档 |
| HTTP 状态码 200/403/404/500 | `http status codes` | MDN Web Docs |
| JSON 是什么 | `json explained` | MDN Web Docs |
| API 是什么（不是 AI） | `what is a web api` | MDN Web Docs |

### 🛠️ 查资料的正确姿势

```
遇到问题的标准流程（按顺序执行）：

1. 先看报错信息的最后一行
   → 复制到 Google / Bing（不要复制全部 traceback）

2. 优先点进：
   ✅ stackoverflow.com
   ✅ 官方文档（docs.python.org / readthedocs.io）
   ✅ realpython.com
   ❌ CSDN（内容质量不稳定，等有能力分辨后再看）
   ❌ 知乎专栏（同上）

3. 如果搜索结果没有匹配的：
   → 说明你的搜索词太具体了，删掉特定变量名/文件名
   → 把具体错误信息替换成通用描述
   
   例：❌ "my_weather_dict[0]['avgtempC'] KeyError"
        ✅ "python KeyError dict key not found"

4. 还是解决不了？
   → 把报错完整信息 + 相关代码片段贴给 AI 工具（ChatGPT / Claude）
```

### 📦 项目四相关链接

| 资源 | 链接 |
|------|------|
| yfinance GitHub | https://github.com/ranaroussi/yfinance |
| yfinance 文档 | https://yfinance-python.org/ |
| Yahoo Finance API 非官方文档 | 搜索 "yahoo finance api v8" |

---

> **最后提醒**：这四个项目从「跑通一个 API」到「读懂一个开源项目」，跨度约 2-3 周。关键是**每个项目都留下「能跑的东西」**——一个 .py 文件、一个 CSV、一个自己写的简化版库。这些就是你面试/简历上的项目证据。
