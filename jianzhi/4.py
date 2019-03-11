#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        row = 0
        collum = len(array[0]) - 1
        while row < len(array) and collum >= 0:
            if array[row][collum] == target:
                return True
            elif array[row][collum] > target:
                collum -= 1
            elif array[row][collum] < target:
                row += 1
        return False
