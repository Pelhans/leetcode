#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        str_num = [str(i) for i in numbers]
        # true 表示 y 比 x 小
        check = lambda x, y: eval(x+y) > eval(y+x)
        for idx in range(1, len(numbers)):
            cur_num = str_num[idx]
            pre_idx = idx - 1
            while not check(cur_num, str_num[pre_idx]) and pre_idx >= 0:
                str_num[pre_idx+1] = str_num[pre_idx]
                pre_idx -= 1
            print "pre_idx: ", pre_idx, cur_num
            str_num[pre_idx+1] = cur_num
            print "str_num: ", str_num
        return "".join(str_num)

print Solution().PrintMinNumber([3, 32, 321])
print Solution().PrintMinNumber([0, 0, 0, 0])
