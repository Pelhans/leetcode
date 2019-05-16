#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-16 09:30:01

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLength = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and usedChar[s[i]] >= start:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength

if __name__=="__main__":
    print(Solution().lengthOfLongestSubstring('arabcacfr'))
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring('bbbbb'))
    print(Solution().lengthOfLongestSubstring('pwwkew'))
