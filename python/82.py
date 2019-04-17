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
       guard = ListNode('x')
       guard.next = head
       p = guard # 用来遍历
       t = guard  # 改变指针指向
       while p:
           if p.next and p.next.val == p.val:
               while p.next and p.next.val == p.val:
                   p = p.next                
               t.next = p.next
               p = p.next               
           else:
               t = p
               p = p.next          
       return guard.next
