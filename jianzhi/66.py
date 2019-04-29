#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return None
        n = len(A)
        C = [1]*n
        D = [1]*n
        B = [1]*n 
        
        for i in range(1, n):
            C[i] = C[i-1]*A[i-1]
        for i in range(0, n-1)[::-1]:
            D[i] = D[i+1]*A[i+1]
        for i in range(n):
            B[i] = C[i]*D[i]
        return B
