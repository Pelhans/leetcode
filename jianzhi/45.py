#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        str_num = [str(i) for i in numbers]
        sort_num = sorted(str_num, cmp= lambda x,y: cmp(x+y,y+x))
        return "".join(sort_num)
