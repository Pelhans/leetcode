#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        elif pNode.right != None:
            pNode = pNode.right
            while pNode.left != None:
                pNode = pNode.left
            return pNode
        elif pNode.next!=None and pNode.next.right==pNode:
            while pNode.next!=None and pNode.next.left!=pNode:
                pNode=pNode.next
            return pNode.next
        else:
            return pNode.next
