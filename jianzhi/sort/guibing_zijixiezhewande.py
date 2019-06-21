#!/usr/bin/env python
# coding=utf-8

def mergeSort(array):
    if not array:
        return []
    if len(array) == 1:
        return array
    mid = len(array) / 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    
    idx_left = 0
    idx_right = 0
    res = []
    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] <= right[idx_right]:
            res.append(left[idx_left])
            idx_left += 1
        else:
            res.append(right[idx_right])
            idx_right += 1
    res.extend(left[idx_left:])
    res.extend(right[idx_right:])
    return res

print mergeSort([1, 3, 2, 5, 7, 2, 5, 6])
