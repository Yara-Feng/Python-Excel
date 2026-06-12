# 项目三：文件批量重命名 CLI

## 🎯 大目标

写一个终端工具，输入文件夹路径和规则，批量重命名文件。支持 `--dry-run` 预览模式（不实际修改）。

## 📋 学习步骤

| 步骤 | 任务 | 输出物 |
|------|------|--------|
| 3.1 | 用 `pathlib.Path.iterdir()` 列出文件夹内所有文件 | 终端打印文件清单 |
| 3.2 | 实现「加前缀」规则：`python rename.py ./test_folder --prefix "IMG_"` | 预览模式下看到新文件名 |
| 3.3 | 实现「按序号编号」规则：`python rename.py ./test_folder --number` | `File.txt` → `001_File.txt` |
| 3.4 | 实现「替换文字」规则：`python rename.py ./test_folder --replace "旧" "新"` | 名称中的文字被替换 |
| 3.5 | 实现 `--dry-run` 预览模式（默认开启，加 `--execute` 才真正改名） | 安全：默认只预览 |
| 3.6 | 用 `argparse` 重构命令行参数 | 完整的 `--help` 输出 |

## 🧠 核心技能

- 命令行参数解析：`argparse`
- 文件系统操作：`pathlib.Path`
- 安全设计思维：`--dry-run` 模式
- 函数组合
- 字符串操作

## ✅ 完成标准

- [ ] `python rename.py --help` 输出完整的帮助信息
- [ ] `python rename.py ./test_folder --prefix "IMG_"` 预览重命名结果
- [ ] `python rename.py ./test_folder --number --execute` 真正改名
- [ ] `python rename.py ./test_folder --replace "旧" "新"` 替换文字
- [ ] 默认 `--dry-run` 模式，不加 `--execute` 不修改任何文件
- [ ] 处理文件名冲突（已存在同名文件时不覆盖，给出警告）
