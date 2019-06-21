#!/usr/bin/env python
# coding=utf-8

"""
数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。
"""

# 不稳定排序，平均 O(nlogn)-O(n^2)，最好 O(nlogn), 最差 O(N**2),辅助空间 O(1)
def shellSort(array):
    if not array:
        return []
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            array = gapInsertSort(array, i, gap)
        gap = gap//2
    return array

def gapInsertSort(array, start, gap):
    for i in range(start+gap, len(array), gap):
        tmp = array[i]
        idx = i
        for j in range(i-gap, 0, -gap):
            if tmp < array[j]:
                array[j+gap] = array[j]
                idx = j
            else:
                break
        array[idx] = tmp
    return array

print shellSort([1,3, 2,5, 4, 5])
