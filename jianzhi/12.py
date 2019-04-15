#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if rows < 0 or cols < 0 or path == None or not matrix:
            return False
        path_index = 0
        bool_matrix = [0]*(cols*rows)
        
        for col in range(cols):
            for row in range(rows):
                if self.juge_path(matrix, rows, cols, row, col, path, path_index, bool_matrix):
                    return True
        return False
    
    def juge_path(self, matrix, rows, cols, row, col, path, path_index, bool_matrix):
        if path_index == len(path):
            return True
        has_path = 0
        
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row*cols+col] == path[path_index] and not bool_matrix[row*cols+col]:
            path_index += 1
            bool_matrix[row*cols+col] = True
            has_path = self.juge_path(matrix, rows, cols, row+1, col, path, path_index, bool_matrix) or \
                        self.juge_path(matrix, rows, cols, row-1, col, path, path_index, bool_matrix) or \
                        self.juge_path(matrix, rows, cols, row, col+1, path, path_index, bool_matrix) or \
                        self.juge_path(matrix, rows, cols, row, col-1, path, path_index, bool_matrix)
            if not has_path:
                path_index -= 1
                bool_matrix[row*cols+col] = False
        return has_path
