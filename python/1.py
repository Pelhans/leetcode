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
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                hash_dict[nums[i]].append(i)
            else:
                hash_dict[nums[i]] = [i]
        for i,j in enumerate(nums):
            if target - j in hash_dict:
                print target - j
                if len(hash_dict[target-j]) == 1 and hash_dict[target-j] != [i]:
                    return [i, hash_dict[target-j][0]]
                elif len(hash_dict[target-j]) == 2:
                    if hash_dict[target-j][0] == i:
                        return [i, hash_dict[target-j][1]]
                    else:
                        return [i, hash_dict[target-j][0]]
