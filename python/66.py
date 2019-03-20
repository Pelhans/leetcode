#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(i) for i in  str(int("".join([str(i) for i in digits]))+1)]
