#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        nodes = [root]
        while nodes:
            stack = []
            for n in nodes:
                if n:
                    res.append(n.val)
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            nodes = stack
        return res
