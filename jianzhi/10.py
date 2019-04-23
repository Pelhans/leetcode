#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        fib1 = 0
        fib2 = 1
        fibN = 0
        for i in range(2, n+1):
            fibN = fib1 + fib2
            fib1 = fib2
            fib2 = fibN
        return fibN
