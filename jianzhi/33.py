#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence)<=0:
            return False
        root = sequence[-1]
        index = 0
        # 为什么这必须加上 -1?否则就超出递归限制
        for i in sequence[:-1]:
            if i > root:
                break
            index += 1
        for i in sequence[index:-1]:
            if i < root:
                return False
        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if index < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return right and left

print Solution().VerifySquenceOfBST([1,3,2,4,7,15,10,5])
