#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-14 21:39:55

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 1:
            return list(ss)
        res = []
        char_list = list(ss)
        char_list.sort()
        for i in range(len(ss)):
            if i > 0 and char_list[i] == char_list[i-1]:
                continue
            tmp = self.Permutation("".join(char_list[:i] + char_list[i+1:]))
            for j in tmp:
                res.append(char_list[i] + j)
        return res
