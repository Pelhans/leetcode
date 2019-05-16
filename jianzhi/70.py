#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# 矩形覆盖 就是斐波那契数列
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        front = 1
        res = 2
        for i in range(3, number+1):
            tmp = res
            res += front
            front = tmp
        return res
