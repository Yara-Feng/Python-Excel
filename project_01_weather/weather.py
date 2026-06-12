"""weather.py — 终端天气预报查询

项目目标：
写一个命令行工具，输入 python weather.py Beijing，
终端打印未来 3 天的天气。
"""

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
