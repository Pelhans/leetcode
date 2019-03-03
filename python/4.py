#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 or len(nums2) == 0:
            nums3 = nums1 + nums2
            if len(nums3) == 0:
                return None
            else:
                if len(nums3) %2 == 0:
                    return (nums3[len(nums3)/2-1] + nums3[len(nums3)/2])/2.0
                else:
                    return nums3[len(nums3)/2]
                    
        new_list = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_list.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                new_list.append(nums2[j])
                j += 1
            else:
                new_list.extend([nums1[i], nums2[j]])
                i += 1
                j += 1
        if i == len(nums1):
            new_list.extend(nums2[j:])
        elif j == len(nums2):
            new_list.extend(nums1[i:])
        len_new = len(new_list)
        if len_new%2 == 0:
            return (new_list[len_new/2 - 1] +  new_list[len_new/2])/2.0
        else:
            return new_list[len_new/2]
