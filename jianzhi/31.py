#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return
        stack = []
        while popV:
            if pushV and popV[0] == pushV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif stack and popV[0] == stack[-1]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV[0])
                pushV.pop(0)
            else:
                return False
        return True
