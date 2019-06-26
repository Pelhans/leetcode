#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def quick_sort(lst, lp, rp):
            if not lst or lp >= rp:
                return lst
            povit = lst[lp]
            left = lp
            right = rp

            while left < right:
                while lst[right] >= povit and left < right:
                    right -= 1
                while lst[left] <= povit and left < right:
                    left += 1
                lst[left], lst[right] = lst[right], lst[left]
            lst[lp], lst[left] = lst[left], lst[lp]
            if left== k:
                return lst
            elif left < k:
                quick_sort(lst, right+1, rp)
            else:
                quick_sort(lst, lp, left-1)
            return lst

        if tinput == [] or k > len(tinput):
            return []
        tinput = quick_sort(tinput, 0, len(tinput)-1)
        return tinput[: k]

print Solution().GetLeastNumbers_Solution([4,5,1,7,2,8,3,12],6)
