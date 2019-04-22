#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = 0
        len2 = 0
        s1 = pHead1
        s2 = pHead2
        while s1:
            len1 += 1
            s1 = s1.next
        while s2:
            len2 += 1
            s2 = s2.next
        diff = abs(len1-len2)
        s1 = pHead1 if len1-len2 >= 0 else pHead2
        s2 = pHead2 if len1-len2 >= 0 else pHead1
        while diff > 0:
            s1 = s1.next
            diff -= 1
        while s1 != s2 and s1 and s2:
            s1 = s1.next
            s2 = s2.next
        return s1
