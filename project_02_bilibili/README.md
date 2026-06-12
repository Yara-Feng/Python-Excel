# 项目二：B站热榜抓取 → CSV

## 🎯 大目标

抓取 B 站热门视频列表，输出到 CSV 文件，包含：排名、标题、播放量、UP 主、视频链接。

## 📋 学习步骤

| 步骤 | 任务 | 输出物 |
|------|------|--------|
| 2.1 | 浏览器访问 `https://api.bilibili.com/x/web-interface/popular` 看懂 JSON | 手写 JSON 结构树 |
| 2.2 | `requests.get()` 拿到数据，打印第一个视频的标题 | 终端输出一个视频标题 |
| 2.3 | `for` 循环遍历所有视频，用 `print` 逐条打印 | 终端列出 100 条视频 |
| 2.4 | 把数据整理成 `list[dict]`，用 `csv.DictWriter` 写入 CSV | 生成 `bilibili_hot.csv` |
| 2.5 | 用 `pandas` 读回 CSV，按播放量排序，打印 Top 10 | 终端输出播放量最高的 10 个视频 |
| 2.6 | 加命令行参数 `--count N` 控制抓取条数 | `python bilibili.py --count 20` |

## 🧠 核心技能

- 带 Header 的 HTTP 请求：`requests` + `headers`
- 嵌套 JSON 数据提取
- CSV 写入：`csv.DictWriter`
- 数据处理：`pandas.read_csv()` `sort_values()` `head()`
- 列表推导 + 数据清洗

## ✅ 完成标准

- [ ] 运行后生成 `bilibili_hot.csv`，可用 Excel 直接打开
- [ ] CSV 中包含 5 个字段（排名、标题、播放量、UP主、链接）
- [ ] 终端输出播放量 Top 10
- [ ] 程序运行时间 < 10 秒
- [ ] 网络不通时有友好提示
