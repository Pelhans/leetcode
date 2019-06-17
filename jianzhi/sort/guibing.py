#!/usr/bin/env python
# coding=utf-8

def guibing(data):
    if len(data) <= 0:
        return
    if len(data) == 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    print "left: ", left

    l1 = guibing(left)
    r1 = guibing(right)

    return merge(l1, r1)

def merge(left, right):
#    print "left: ", left
    if not left or not right:
        return left + right
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result

print guibing([5,4 ,3 ,2 ,1])
