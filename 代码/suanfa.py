# def merge(left_array, right_array):
#     """
#     对数组left_array和right_array进行归并
#     """
#     temp_array = []  # 新的已排序好的临时列表
#     left_index = 0  # left_array列表的下标
#     right_index = 0  # right_array列表的下标
#     while left_index < len(left_array) and right_index < len(right_array):
#         """
#         对两个列表中的元素 两两对比，将最小的元素，放到result中，并对当前列表下标加1
#         """
#         if left_array[left_index] <= right_array[right_index]:  # 如果左边的值小于等于右边的值
#             temp_array.append(left_array[left_index])  # 临时数组加入左边的值
#             left_index += 1  # left_array数组的下标+1
#         else:
#             temp_array.append(right_array[right_index])  # 临时数组加入右边的值
#             right_index += 1  # right_array数组的下标+1
#     temp_array += left_array[left_index:]
#     temp_array += right_array[right_index:]
#     return temp_array
#
#
# def merge_sort(array):
#     """
#     对数组array进行拆分
#     """
#     if len(array) <= 1:  # 如果数组的元素少于或只有一个
#         return array  # 直接把数组返回
#     middle = int(len(array) / 2)  # 把数组进行拆分
#     left_array = merge_sort(array[:middle])  # 左边的数组
#     right_array = merge_sort(array[middle:])  # 右边的数组
#     return merge(left_array, right_array)  # 对排序好的两个列表合并，产生一个新的排序好的列表
#
# import random
# l3 = [random.randint(1,1000) for i in range(10000)]
# print(l3)
# l4 = merge_sort(l3)
# print(l4)
def mergesort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


a = [1, 15, 12, 3, 56, 42, 1, 44, 32, 25, 6, 7, 32]
a = mergesort(a)
print("result:" + str(a))