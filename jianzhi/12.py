#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or cols < 0 or rows < 0 or not path:
            return False
        markmatrix = [0]*(rows*cols)
        init_pos = []
        for i,j in enumerate(matrix):
            if j == path[0]:
                init_pos.append(i)
        if not init_pos:
            return False
        step = 1
        for i,j in enumerate(init_pos):
            self.juge_path(j, matrix, rows, cols, path, step, markmatrix)
    def juge_path(self, pos, matrix, rows, cols, path, step, markmatrix):
        if step == len(path):
            return True
        if pos-cols >=0 and markmatrix[pos-cols] == 0 and path[step] == matrix[pos-cols]:
            markmatrix[pos-cols] = 1
            step += 1
            return self.juge_path(pos-cols, matrix, rows, cols, path, step, markmatrix)
        elif pos+cols <=rows*cols-1 and markmatrix[pos+cols] == 0 and path[step] == matrix[pos+cols]:
            step += 1
            markmatrix[pos+cols] = 1
            return self.juge_path(pos+cols, matrix, rows, cols, path, step, markmatrix)
        elif pos+1 <=rows*cols-1 and (pos+1)%cols != 0 and markmatrix[pos+1] == 0 and path[step] == matrix[pos+1]:
            step += 1
            markmatrix[pos+1] = 1
            return self.juge_path(pos+1, matrix, rows, cols, path, step, markmatrix)
        elif pos-1 >=0 and pos%cols != 0 and markmatrix[pos-1] == 0 and path[step] == matrix[pos-1]:
            step += 1
            markmatrix[pos-1] = 1
            return self.juge_path(pos-1, matrix, rows, cols, path, step, markmatrix)
        else:
            return False
