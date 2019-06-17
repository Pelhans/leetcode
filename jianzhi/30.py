#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.min_stack == [] or self.min() > node:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min())
            
    def pop(self):
        # write code here
        if self.min_stack == [] or self.stack == []:
            return None
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        # write code here
        return self.stack[-1]
    
    def min(self):
        # write code here
        return self.min_stack[-1]
