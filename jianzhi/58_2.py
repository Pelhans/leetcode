#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s) <= 0:
            return ""
        if s.strip() == "":
            return s
        sen_reverse = self.reverse(s)
        token_reverse = " ".join([self.reverse(i) for i in sen_reverse.split()])
        return token_reverse
        
    def reverse(self, list_s):
        if isinstance(list_s, str) and not isinstance(list_s, list):
            list_s = list(list_s)
        start = 0
        end = len(list_s) - 1
        while start < end:
            list_s[start], list_s[end] = list_s[end], list_s[start]
            start += 1
            end -= 1
        return "".join(list_s)
