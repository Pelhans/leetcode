#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        return self.Sum_Solution(n-1) + n
