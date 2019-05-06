#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 原地排序，维护一个指针指向原地新数组的尾部，另一个正常走。数组问题往前查重
        if len(nums) <=2:
            return len(nums)
        index = 2
        for i in range(2,len(nums)):
            if nums[index-2] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index
