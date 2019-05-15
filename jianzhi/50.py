#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-15 18:53:57

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) <= 2:
            return
        from collections import Counter
        l = Counter(array)
        return [i for i in l if l[i] == 1]
