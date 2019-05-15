#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-15 16:26:34

# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s and len(s) < 1:
            return False
        s = s.lower()
        if s.count("e") > 1:
            return False
        if "e" in s:
            ide = s.index("e")
            return self.isDigit(s[:ide]) and self.isDigit(s[ide+1:], check_int=True)
        else:
            return self.isDigit(s)
    
    def isDigit(self, s, check_int=False, allow_sign=True):
        if len(s) == 0:
            return False
        if check_int and s.count(".") > 0:
            return False
        if s.count(".") > 1:
            return False
        if allow_sign:
            if s[1:].count("+") or s[1:].count("-"):
                return False
        allow_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "."]
        for i in s:
            if i not in allow_char:
                return False
        return True
