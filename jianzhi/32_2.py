#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        level = 0
        nodes = [pRoot]
        result = []
        while nodes:
            level += 1
            cur_stack = []
            next_stack = []
            for n in nodes:
                cur_stack.append(n.val)
                if n.left:
                    next_stack.append(n.left)
                if n.right:
                    next_stack.append(n.right)
            if level % 2 == 0:
                cur_stack.reverse()
            nodes = next_stack
            result.append(cur_stack)
        return result
