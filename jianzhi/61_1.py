#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        num_zero = numbers.count(0)
        for i in range(len(numbers)-1):
            v = numbers[i]
            if v == 0:
                continue
            if v == numbers[i+1]:
                return False
            num_zero -= (numbers[i+1] - v - 1)
            if num_zero < 0:
                return False
        return True
