#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def Print1ToMaxOfNDigits(self, n):
        if n <= 0:
            return False
        number = ['0']*n
        for i in range(10):
            number[0] = str(i)
            self.print1ToMaxN(number, n, 0)

    def print1ToMaxN(self, number, length, index):
        if index == length - 1:
            self.printNumber(number)
            return

        for i in range(10):
            number[index+1] = str(i)
            self.print1ToMaxN(number, length, index+1)

    def printNumber(self, number):
        begin = 0
        for i,j in enumerate(number):
            if j != "0":
                begin = i
                break
        print "".join(number[begin:])

if __name__ == "__main__":
    Solution().Print1ToMaxOfNDigits(3)
