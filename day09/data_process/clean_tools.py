"""数据清洗模块"""

def remove_duplicates(data: list) -> list:
    """去除列表中的重复元素，保持顺序"""
    seen = set()
    result = []
    for item in data:
        if item not in result:
            seen.add(item)
            result.append(item)
    return result

def drop_null(data: list) -> list:
    """去除列表中的空值（None、空字符串、空列表等）"""
    return [item for item in data if item]