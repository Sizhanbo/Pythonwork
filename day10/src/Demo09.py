


def error_log_counter(file_path):
    """统计日志中包含error的行数（生成器版）"""
    count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:  # 文件对象本身是可迭代对象，逐行读取
            print(line.strip())
            if "error" in line.lower():
                count += 1
                yield count  # 实时返回统计结果

# 使用生成器（实时查看统计进度）
for count in error_log_counter("../log/large_log.txt"):
    print(f"已找到 {count} 条错误日志")