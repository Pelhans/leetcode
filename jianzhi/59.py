#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size < 1:
            return[]
        if num < size:
            return [max(num)]
        res = []
        for i in range(len(num)-size+1):
            res.append(max(num[i:i+size]))
        return res
