#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_str = {}
        start_idx = 0
        max_len = 0
        for i, j in enumerate(s):
            if j not in max_str:
                max_str[j] = i
                if max_len < len(max_str):
                    max_len = len(max_str)
            else:
                repeat = max_str[j]           
                for m in s[start_idx:repeat+1]:
                    max_str.pop(m)
                start_idx = repeat+1
                max_str[j] = i
        return max_len
