#!/usr/bin/env python
# coding=utf-8

# 空间复杂度太高

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix or len(matrix)<=0 or len(matrix[0])<=0:
            return []
        row = len(matrix)
        col = len(matrix[0])
        rrow = 0
        rcol = 0
        markMatrix = [False]*(col*row)
        outList = []
        while False in markMatrix:
            outList.append(matrix[rrow][rcol])
            markMatrix[rrow*col+rcol] = True
            bool_up = self.check_site(rrow-1, rcol, row, col, markMatrix)
            bool_down = self.check_site(rrow+1, rcol, row, col, markMatrix)
            bool_left = self.check_site(rrow, rcol-1, row, col, markMatrix)
            bool_right = self.check_site(rrow, rcol+1, row, col, markMatrix)
            if not bool_up and not bool_left and bool_down and bool_right:
                rcol += 1
            elif not bool_up and not bool_left and bool_down and not bool_right:
                rrow += 1
            elif not bool_up and bool_left and not bool_down and not bool_right:
                rcol -= 1
            elif bool_up and not bool_left and not bool_down and not bool_right:
                rrow -= 1
        return outList
    
    def check_site(self, row, col, lrow, lcol, markMatrix):
        if row >= 0 and row < lrow and col >= 0 and col < lcol:
            if  markMatrix[row*lcol+col] == False:
                return True
            else:
                return False
        else:
            return False
