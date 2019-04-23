#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        cur_sum = 0
        max_sum = float('-inf')
        for i in range(len(array)):
            if i == 0 or cur_sum <= 0:
                cur_sum = array[i]
            elif i != 0 and cur_sum > 0:
                cur_sum += array[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
