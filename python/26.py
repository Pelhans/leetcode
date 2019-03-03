#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count = count + 1
                nums[count] = nums[i]
        return count +1
