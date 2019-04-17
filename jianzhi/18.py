#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        guard = ListNode('x')
        guard.next = pHead
        p = guard
        t = guard
        
        while p:
            if p.next and p.val == p.next.val:
                while p.next and p.next.val == p.val:
                    p = p.next
                t.next = p.next
                p = p.next
            else:
                t = p
                p = p.next
        return guard.next
