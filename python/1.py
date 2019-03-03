#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return None
        hash_dict = {nums[i]:i for i in range(len(nums))}
        result = []
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in hash_dict and hash_dict[gap] > i:
                result.extend([i, hash_dict[gap]])
        return result
