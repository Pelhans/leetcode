#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# 变态跳台阶
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 1 << (number-1)
