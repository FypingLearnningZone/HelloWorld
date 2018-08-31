from collections import deque

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged,left,right = [],deque(left),deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return merged

    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

import random
l1 = [random.randint(1,100) for i in range(4)]
print(l1)

l2 = merge_sort(l1)
print(l2)