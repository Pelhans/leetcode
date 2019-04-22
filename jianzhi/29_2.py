#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        while cols > 2*start and rows > 2*start:
            self.printNum(matrix, rows, cols, start, res)
            start += 1
        return res
    
    def  printNum(self, matrix, rows, cols, start, res):
        endCol = cols - start - 1
        endRow = rows - start - 1
        
        for i in range(start, endCol):
            res.append(matrix[start][i]) 
        for i in range(start, endRow):
            res.append(matrix[i][endCol])
        for i in range(start, endCol)[::-1]:
            res.append(matrix[endRow][i])
        for i in range(start,endRow)[::-1]:
            res.append(matrix[i][start])
