import pandas as pd

def M01_read_and_clean(file_path):
    """
    【输入】：Excel文件的绝对路径 (字符串)
    【输出】：干净的内存数据表 (DataFrame)
    """
    # 读取Excel，自动将数字转换为字符串防止变形，去掉全空行
    df = pd.read_excel(file_path).dropna(how='all')
    
    # 清理所有文本前后的看不见的空格
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
        
    return df