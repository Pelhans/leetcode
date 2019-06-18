#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        nodes = [pRoot]
        res = []
        while nodes:
            cur_stack = []
            next_stack = []
            for n in nodes:
                cur_stack.append(n.val)
                if n.left:
                    next_stack.append(n.left)
                if n.right:
                    next_stack.append(n.right)
            nodes = next_stack
            res.append(cur_stack)
        return res
