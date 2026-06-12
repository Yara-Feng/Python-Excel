"""rename.py — 批量文件重命名工具

项目目标：
写一个终端工具，输入文件夹路径和规则，批量重命名文件。
支持 --dry-run 预览模式（不实际修改）。
"""

import argparse
from pathlib import Path


def list_files(folder: Path) -> list:
    """返回文件夹内所有文件的路径列表（不含子目录）"""
    return [f for f in folder.iterdir() if f.is_file()]


def preview_rename(folder: Path, old_name: str, new_name: str) -> None:
    """打印重命名预览"""
    print(f"  {old_name}  →  {new_name}")


def execute_rename(folder: Path, old_name: str, new_name: str) -> None:
    """实际执行重命名"""
    (folder / old_name).rename(folder / new_name)
    print(f"  ✓ {old_name}  →  {new_name}")


def add_prefix(files: list, prefix: str) -> list:
    """为所有文件加前缀"""
    # TODO: 返回 [(旧名, 新名), ...]
    return [(f.name, prefix + f.name) for f in files]


def replace_text(files: list, old: str, new: str) -> list:
    """替换文件名中的文字"""
    # TODO
    pass


def number_files(files: list) -> list:
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
