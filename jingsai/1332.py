#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        dl = defaultdict(list)
        for r in range(R):
            for c in range(C):
                dis = abs(r - r0) + abs(c - c0)
                dl[dis].append([r,c])
        output = []
        for i in dl:
            output.extend(dl[i])
        return output
