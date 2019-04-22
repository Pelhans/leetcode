#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum = 0
        for demo in J:
            sum += S.count(demo)
        return sum
