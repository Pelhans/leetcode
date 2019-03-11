#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = str(N)
        oper = ["*", "/", "+", "-"]
        idxo = 0
        while N-1 > 0:
            num = num + oper[idxo] + str(N-1)
            if idxo == 3:
                idxo = 0
            else:
                idxo += 1
            N -= 1
        return eval(num)
