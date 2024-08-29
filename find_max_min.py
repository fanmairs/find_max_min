def find_max_min(arr):
    if not arr:
        return "数组为空"
    
    # 初始化最大值和最小值
    # max_first = arr[0]
    # min_first = arr[0]
    max_first,min_first = arr[0],arr[0]
    
    # 遍历数组，找出最大值和最小值
    for num in arr[1:]:
        if num > max_first:
            max_first = num
        if num < min_first:
            min_first = num
    
    return max_first, min_first

# 测试代码
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_max_min(arr))  # 输出: (9, 1)

empty_arr = []
print(find_max_min(empty_arr))  # 输出: 数组为空