#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <=0 :
            return 0
        res = [1]
        p = 1
        t2 = 0
        t3 = 0
        t5 = 0
        
        while p < index:
            M = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(M)
            while 2*res[t2] <= M:
                t2 += 1
            while 3*res[t3] <= M:
                t3 += 1
            while 5*res[t5] <= M:
                t5 += 1
            p += 1
        return res[index-1]
