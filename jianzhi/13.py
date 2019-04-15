#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows < 1 or cols < 1 or threshold < 0:
            return 0
        
        bool_matrix = [False]*(rows*cols)
        count = self.juge_enter(threshold, rows, cols, 0, 0, bool_matrix)
        return count
    
    def juge_enter(self, threshold, rows, cols, row, col, bool_matrix):
        enter = 0
        if self.check_sum(row) + self.check_sum(col) <= threshold and col >=0 and col < cols and row >= 0 and row < rows and not bool_matrix[row*cols+col]:
            bool_matrix[row*cols+col] = True
            enter = 1 + self.juge_enter(threshold, rows, cols, row+1, col, bool_matrix) + \
                    self.juge_enter(threshold, rows, cols, row-1, col, bool_matrix) + \
                    self.juge_enter(threshold, rows, cols, row, col+1, bool_matrix)+ \
                    self.juge_enter(threshold, rows, cols, row, col-1, bool_matrix)
        return enter
    
    def check_sum(self, num):
        sum = 0
        while num > 0:
            sum += num % 10
            num = num / 10
        return sum
