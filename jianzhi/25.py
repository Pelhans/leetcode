#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        mergeNode = ListNode(0)
        if pHead1.val < pHead2.val:
            mergeNode.val = pHead1.val
            mergeNode.next = self.Merge(pHead1.next, pHead2)
        else:
            mergeNode.val = pHead2.val
            mergeNode.next = self.Merge(pHead1, pHead2.next)
        return mergeNode
