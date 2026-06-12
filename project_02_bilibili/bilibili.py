"""bilibili.py — B站热门视频抓取，输出 CSV

项目目标：
抓取 B 站热门视频列表，输出到 CSV 文件，包含：
排名、标题、播放量、UP 主、视频链接。
"""

import csv
import requests
import pandas as pd

API_URL = "https://api.bilibili.com/x/web-interface/popular"


def fetch_hot_videos() -> list:
    """抓取 B 站热门视频列表，返回清洗后的数据"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.bilibili.com/",
    }
    r = requests.get(API_URL, headers=headers, timeout=15)
    r.raise_for_status()
    data = r.json()
    
    # TODO: 从 data 中提取视频列表
    videos = data["data"]["list"]
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


def save_to_csv(videos: list, filename: str = "bilibili_hot.csv"):
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
