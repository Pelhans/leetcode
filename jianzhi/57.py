#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2:
            return []
        result = []
        out_put = []
        set_array = set(array)
#        for i in range(len(array)):
        i = 0
        while i < len(array)-1:
            if tsum - array[i] in set_array:
                if tsum - array[i] == array[i]:
                    if array.count(array[i]) > 1:
                        result.append([array[i], array[i]])
                else:
                    result.append([array[i], tsum - array[i]])
            if tsum - array[i] < array[i]:
                break
            i += 1
        if len(result) > 0:
            result = sorted(result, key=lambda a: a[0]*a[1])
            return result[0][0], result[0][1]
        else:
            return []
