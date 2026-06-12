"""mini_yfinance.py — 极简版 Yahoo Finance 数据获取

项目目标：
读懂 yfinance 源码，实现一个简化版的股票数据获取工具。
"""

import requests
import pandas as pd


def get_stock_history(ticker: str, period: str = "1mo") -> pd.DataFrame:
    """
    获取美股历史行情。
    
    Args:
        ticker: 股票代码，如 "AAPL"
        period: 时间范围，如 "1mo", "3mo", "1y"
    
    Returns:
        包含股票行情数据的 DataFrame
    """
    # TODO: 参考 yfinance 源码，实现核心逻辑
    # 1. 构造请求 URL
    # 2. requests.get()
    # 3. 解析 JSON
    # 4. 转为 DataFrame 并清洗
    pass


if __name__ == "__main__":
    # 测试
    df = get_stock_history("AAPL")
    print(df.head(10))
