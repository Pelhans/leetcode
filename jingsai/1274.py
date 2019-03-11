#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                left = self.bstFromPreorder(preorder[1:i])
                right = self.bstFromPreorder(preorder[i:])
                root.left = left
                root.right = right
                return root
        left = self.bstFromPreorder(preorder[1:])
        right = None
        root.left = left
        root.right = right
        return root
        
