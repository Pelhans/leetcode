#!/usr/bin/env python
# coding=utf-8

# 青蛙跳台阶
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        f2 = 1
        res = 2
        for i in range(3, number+1):
            tmp = res
            res += f2
            f2 = tmp
        return res
