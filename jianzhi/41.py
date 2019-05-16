#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return n
        sum = 0
        for i in range(n):
            if "1" in str(i):
                sum += str(i).count("1")
        return sum

print(Solution().NumberOf1Between1AndN_Solution(5))
