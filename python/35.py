#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_num = len(nums)
        while len_num > 0:
            len_num /= 2
            if target == nums[len_num]:
                return len_num
            elif target < nums[len_num]:
                if len(nums) == 1:
                    return 0
                if target > nums[len_num-1]:
                    return len_num
                else:
                    return self.searchInsert(nums[:len_num], target)
            elif target > nums[len_num]:
                if len(nums) <= 2:
                    return len_num + 1
                if target < nums[len_num+1]:
                    return len_num+1
                else:
                    return len_num + 1 + self.searchInsert(nums[len_num+1:], target)
