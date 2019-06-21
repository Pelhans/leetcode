#!/usr/bin/env python
# coding=utf-8

"""
    1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2. 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
    3. 针对所有的元素重复以上的步骤，除了最后一个。
    4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较.
"""

# 稳定排序，平均 O(n**2)，最好 O(N), 最差 O(N**2),辅助空间 O(1)
def bubble_sort(array):
    if not array:
        return []
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                tmp = array[j-1]
                array[j-1] = array[j]
                array[j] = tmp
            else:
                continue
    return array

print bubble_sort([1, 3, 2, 5, 4])
