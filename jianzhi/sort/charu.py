#!/usr/bin/env python
# coding=utf-8

"""
   1. 从第一个元素开始，该元素可以认为已经被排序
   2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
   3. 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
   4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
   5. 将新元素插入到该位置后
   6. 重复步骤2~5
"""

# 稳定排序，平均 O(n**2)，最好 O(N), 最差 O(N**2),辅助空间 O(1)

def insertSort(array):
    for i in xrange(len(array)):
        tmp = array[i]
        idx = i
        for j in xrange(i, 0, -1):
            if tmp < array[j-1]:
                array[j] = array[j-1]
                idx = j - 1
            else:
                break
        array[idx] = tmp
    return array

print insertSort([1, 3, 2, 5, 4])

