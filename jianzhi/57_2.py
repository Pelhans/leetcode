#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (1+tsum)/2
        cursum = small + big
        res = []
        while small < middle:
            if cursum == tsum:
                res.append(range(small, big+1))
            while cursum > tsum and small < middle:
                cursum -= small
                small += 1
                if cursum == tsum:
                    res.append(range(small, big+1))
            big += 1
            cursum += big
        return res
