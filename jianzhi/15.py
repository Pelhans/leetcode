#!/usr/bin/env python
# coding=utf-8

class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n&0xffffffff).count("1")
