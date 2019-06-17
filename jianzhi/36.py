#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        self.path = []
        self.inOrder(pRootOfTree)
        for i,v in enumerate(self.path[:-1]):
            self.path[i].right = self.path[i+1]
            self.path[i+1].left = v
        return self.path[0]
        
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.path.append(root)
        self.inOrder(root.right)
