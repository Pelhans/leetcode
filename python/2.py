#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_l1 = 0
        num_l2 = 0
        exp = 1
        while l1 is not None:
            num_l1 = l1.val * exp + num_l1
            l1 = l1.next
            exp *= 10
        exp = 1
        while l2 is not None:
            num_l2 = l2.val * exp + num_l2
            l2 = l2.next
            exp *= 10
        result = str(num_l1 + num_l2)[::-1]
        print result
        l3 = ListNode(int(result[0]))
        cur = l3
        for i in result[1:]:
            next = ListNode(int(i))
            cur.next= next
            cur = next
        return l3
