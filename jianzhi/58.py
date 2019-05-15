#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-15 17:31:45


# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s) <= 0:
            return ""
        if len(s) <= n:
            return s
        return self.reverse(self.reverse(s[:n])+self.reverse(s[n:]))
    
    def reverse(self, s):
        if not isinstance(s, list):
            s = list(s)
        start = 0
        last = len(s) - 1
        while start < last:
            s[start], s[last] = s[last], s[start]
            start += 1
            last -= 1
        return "".join(s)
