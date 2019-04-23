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
        if head is None or head.next is None:
            return head
        guard = ListNode('x')
        guard.next = head
        pre = guard
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                num = cur.val
                while cur.next and num == cur.next.val:
                    cur = cur.next
                pre.next = cur
                pre = cur
                cur = cur.next
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return guard.next
