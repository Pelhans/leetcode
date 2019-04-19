#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        preNode = None
        curNode = pHead
        newHead = None
        if not pHead or not pHead.next:
            return pHead
        while curNode:
            lastNode = curNode.next
            if lastNode is None:
                newHead = curNode
            curNode.next = preNode
            preNode = curNode
            curNode = lastNode
        return newHead
