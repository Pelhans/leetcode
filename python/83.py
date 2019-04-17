#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        p = head
        while p.next != None:
            if p.val == p.next.val:
                if p.next.next != None:
                    p.next = p.next.next
                else:
                    p.next = None
            else:
                p = p.next
        return head
