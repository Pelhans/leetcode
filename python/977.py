#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A = [i**2 for i in A]
        return sorted(A)
