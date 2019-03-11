#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        ns = ""
        for i in s:
            if i == " ":
                ns += "%20"
            else:
                ns += i 
        return ns
