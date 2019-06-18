#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            sum_ = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2)<<1)& 0xffffffff
            num1 = sum_
            num2 = carry
        if num1<0x7fffffff:
            return num1
        else:
            return ~(num1^0xffffffff)
