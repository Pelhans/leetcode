#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) <= 0:
            return 0
        if len(tinput) < k:
            return tinput
        min_k = ["inf" for i in range(k)]
        for i in tinput:
            if i > min_k[-1]:
                continue
            if i < min_k[-1]:
                self.insertNum(min_k, i)
        return min_k
    
    def insertNum(self, min_k, num):
        for i in range(len(min_k)):
            if num < min_k[i]:
                min_k.insert(i, num)
                min_k.pop()
                break
        return min_k

print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],8))
