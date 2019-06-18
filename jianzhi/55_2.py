#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def dfs(self, pRoot):
        if not pRoot:
            return 0
        left = self.dfs(pRoot.left)
        right = self.dfs(pRoot.right)
        return max(left, right) + 1
    
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.dfs(pRoot.left)
        right = self.dfs(pRoot.right)
        if abs(left - right) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
