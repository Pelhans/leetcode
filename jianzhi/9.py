#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        # write code here
        return self.stackA.append(node)
    def pop(self):
        # return xx
        if self.stackA == []:
            return False
        elif len(self.stackA) == 1:
            return self.stackA.pop(0)
        self.stackB = [self.stackA[0]]
        self.stackA = self.stackA[1:]
        return self.stackB[0]
