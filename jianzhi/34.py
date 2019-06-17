#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root :
            return []
        result = []
        
        def dfs(root, path, currentNumber):
            currentNumber += root.val
            path.append(root)
            flag = (not root.left and not root.right)
            
            if flag and currentNumber == expectNumber:
                tmp_path = []
                for p in path:
                    tmp_path.append(p.val)
                result.append(tmp_path)
            if currentNumber < expectNumber:
                if root.left:
                    dfs(root.left, path, currentNumber)
                if root.right:
                    dfs(root.right, path, currentNumber)
            path.pop()
        dfs(root, [], 0)
        return result
