#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        while listNode is not None:
            result.append(listNode.val)
            listNode = listNode.next
        result.reverse()
        return result
