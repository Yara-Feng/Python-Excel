def M17_split_by_column(df, split_column):
    """
    【输入】：内存数据表(df)，依据的列名(字符串)
    【输出】：一个字典，里面是一堆小表。格式为 { '销售一部': 小表1, '销售二部': 小表2 }
    """
    grouped = df.groupby(split_column)
    split_results = {str(key): group for key, group in grouped}
    return split_results