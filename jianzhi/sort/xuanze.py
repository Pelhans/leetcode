#!/usr/bin/env python
# coding=utf-8

"""
    1. 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3. 以此类推，直到所有元素均排序完毕。
"""

# 不稳定排序，平均 O(n**2)，最好 O(N**2), 最差 O(N**2),辅助空间 O(1)
def select_sort(array):
    for i in range(len(array)):
        idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[idx]:
                idx = j
        array[idx], array[i] = array[i], array[idx]
    return array

print select_sort([1, 3, 2, 5, 4])
            
