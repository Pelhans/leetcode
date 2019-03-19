#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        elif len(rotateArray) == 2:
            return min(rotateArray[0], rotateArray[1])
        
        if rotateArray[len(rotateArray)/2] < rotateArray[0]:
            return self.minNumberInRotateArray(rotateArray[:len(rotateArray)/2+1])
        elif rotateArray[len(rotateArray)/2] > rotateArray[-1]:
            return self.minNumberInRotateArray(rotateArray[len(rotateArray)/2:])
