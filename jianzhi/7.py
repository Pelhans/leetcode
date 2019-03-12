#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0])
        
        root.left = self.reConstructBinaryTree(pre[1:val+1], tin[:val])
        root.right = self.reConstructBinaryTree(pre[val+1:], tin[val+1:])
        return root
