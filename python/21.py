#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        b = l1 if l1.val < l2.val else l2
        s = l2 if l1.val < l2.val else l1
        if b:
          b.next = self.mergeTwoLists(b.next, s)
        return b
