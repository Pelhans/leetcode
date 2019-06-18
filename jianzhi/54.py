#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.res = []
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k < 1:
            return 
        self.mid(pRoot)
        if k > len(self.res):
            return
        return self.res[k-1]
    def mid(self, pRoot):
        if not pRoot:
            return
        self.mid(pRoot.left)
        self.res.append(pRoot)
        self.mid(pRoot.right)
