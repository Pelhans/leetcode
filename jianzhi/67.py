#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-15 16:46:17

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0:
            return 0
        allow_num = [str(i) for i in range(10)]
        sign = 1
        sum = 0
        for i in range(len(s)):
            if i == 0:
                if s[i] == "-":
                    sign = -1
                    continue
                elif s[i] == "+":
                    continue
            if s[i] in allow_num:
                sum = sum*10 + allow_num.index(s[i])
            else:
                sum = 0
                break
        return sum*sign
