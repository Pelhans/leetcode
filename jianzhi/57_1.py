#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2:
            return []
        fnum = 0
        lnum = len(array)-1
        while fnum != lnum:
            sum_total = array[fnum] + array[lnum]
            if sum_total == tsum:
                return [array[fnum], array[lnum]]
            elif sum_total > tsum:
                lnum -= 1
            elif sum_total < tsum:
                fnum += 1
        return []
