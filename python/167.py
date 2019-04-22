#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        out = []
        setnum = set(numbers)
        for i in range(len(numbers)):
            if target - numbers[i] in setnum:
                if i != numbers.index(target-numbers[i]):
                    out.extend([i+1, numbers.index(target-numbers[i])+1])
                    return sorted(out)
        return None
