#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for num in array:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return odd+even
