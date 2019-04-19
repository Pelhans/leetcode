#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast_p = pHead
        slow_p = pHead
        if pHead is None:
            return Null
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if slow_p == fast_p:
                break
        if fast_p is None or fast_p.next is None:
            return None
        fast_p = pHead
        while fast_p != slow_p:
            fast_p = fast_p.next
            slow_p = slow_p.next
        return fast_p
