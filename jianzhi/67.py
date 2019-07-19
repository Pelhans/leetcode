#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-15 16:46:17

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0:
            return 0
        
        nums = s.strip().split("e")
        if len(nums) > 2:
            return False
        isnum = True
        for n in nums:
            isnum &= self.check_num(n)
        if isnum:
            return self.trans(s)
        else:
            return 0
    
    def trans(self, s):
        
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        nums = s.strip().split("e")
        res = 0
        base = 0
        for num in nums:
            tmp_res = 0
            sign = 1
            if s[0] == "-":
                sign = -1
            for i in num:
                if i in ["+", "-"]:
                    continue
                tmp_res = tmp_res*10 + numbers.index(i)
            if base == 0:
                base = tmp_res*sign
                res = base
            else:
                res = pow(base, tmp_res*sign)
        return res
    def check_num(self, num):
        sign = False
        if len(num) == 1 and num[0] in ["-", "+"]:
            return False
        for i in range(1, len(num)):
            if num[i].isalpha():
                return False
            if not num[i].isalnum():
                return False
        return True
