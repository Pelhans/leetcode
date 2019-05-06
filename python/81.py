#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if target == nums[0]:
                return True
            else:
                return False
        first = 0
        last = len(nums)
        while first != last:
            mid = first +(last-first)/2
            if nums[mid] == target:
                return True
            if nums[first] < nums[mid]:
                if target >= nums[first] and target < nums[mid]:
                    last = mid
                else:
                    first = mid + 1
            elif nums[mid] < nums[first]:
                if target > nums[mid] and target <= nums[last-1]:
                    first = mid + 1
                else:
                    last = mid
            else:
                first += 1
        return False
