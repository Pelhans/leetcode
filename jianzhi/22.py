#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        fast_p = head
        slow_p = head
        if head is None or k <= 0:
            return None
        for i in range(k-1):
            if fast_p.next is None:
                return None
            fast_p = fast_p.next
        while fast_p.next is not None:
            fast_p = fast_p.next
            slow_p = slow_p.next
        return slow_p
