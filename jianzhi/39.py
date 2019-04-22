#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers or len(numbers) <= 0:
            return None
        res = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                res = numbers[i]
                times = 1
            elif res == numbers[i]:
                times += 1
            else:
                times -= 1
        
        sum = 0
        for i in range(len(numbers)):
            if res == numbers[i]:
                sum += 1
        return res if sum*2 > len(numbers) else 0
