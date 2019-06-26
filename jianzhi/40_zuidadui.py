#!/usr/bin/env python
# coding=utf-8

#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k > len(tinput) or k==0:
            return []
        def maxHeap(tinput):
            for i in range(len(tinput), -1, -1):
                if 2*i +1 > len(tinput) and 2*i +2 > len(tinput):
                    continue
                left = 2*i +1
                right = 2*i + 2
                idx = i
                if left < len(tinput) and tinput[left] > tinput[i]:
                    idx = left
                if right < len(tinput) and tinput[right] > tinput[i]:
                    idx = right
                tinput[i], tinput[idx] = tinput[idx], tinput[i]
            for i in range(len(tinput)):
                if 2*i +1 > len(tinput) and 2*i +2 > len(tinput):
                    continue
                left = 2*i + 1
                right = 2*i + 2
                idx = i
                if left < len(tinput) and tinput[left] > tinput[i]:
                    idx = left
                if right < len(tinput) and tinput[right] > tinput[i]:
                    idx = right
                tinput[i], tinput[idx] = tinput[idx], tinput[i]
            return tinput
        k_head = [float("inf")]*k
        for num in tinput:
            if num < k_head[0]:
                k_head[0] = num
                k_head = maxHeap(k_head)
#        k_head.sort()
        return k_head

print Solution().GetLeastNumbers_Solution([4, 3, 5, 6, 1, 2, 7], 5)

