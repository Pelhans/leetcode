#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        first = 0
        last = len(nums)
        while first != last:
            mid = first + (last-first)/2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[first]:
                if nums[mid] > target and nums[first] <= target:
                    last = mid
                else:
                    first = mid + 1
            else:
                if nums[mid] <target and target <= nums[last-1]:
                    first = mid + 1
                else:
                    last = mid
        return -1
