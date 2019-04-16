#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent < 0:
            return 0
            raise ValueError("Wrong Input")
        if exponent >= 0:
            return self.compute_power(base, exponent)
        return 1.0/self.compute_power(base, -exponent)
    
    def compute_power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.compute_power(base, exponent>>1)
        res *= res
        if exponent & 0x1 == 1:
            res *= base
        return res
