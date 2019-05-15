#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-15 18:58:24

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        from collections import Counter
        freq_dict = Counter(s)
        for idx, char in enumerate(s):
            if freq_dict[char] == 1:
                return idx
        return -1
