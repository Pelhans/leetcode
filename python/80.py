#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        count = 1
        end = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count += 1
                if count <= 2:
                    nums[end] = nums[i]
                    end += 1
            else:
                count = 1
                nums[end] = nums[i]
                end += 1
        return end
