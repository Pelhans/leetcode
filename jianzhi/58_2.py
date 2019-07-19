#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ""
        first = self.reverse(s)
        second = []
        for i in first.split(" "):
            second.append(self.reverse(i))
        return " ".join(second)
        
    def reverse(self, s):
        return "".join(list(s)[::-1])
