#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ Pelahs 2019-05-15 18:38:25

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0 or k is None:
            return 
        first = self.getFirst(data, k)
        last = self.getLast(data, k)
        if last > -1 and first > -1:
            return last - first + 1
        return
    
    def getFirst(self, data, k):
        start = 0
        end = len(data)-1
        
        while start <= end:
            mid = (end+start)/2
            if data[mid] == k:
                if  mid - 1 >= 0 and data[mid-1] == data[mid]:
                    end = mid - 1
                else:
                    return mid
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    def getLast(self, data, k):
        start = 0
        end = len(data)-1
        
        while start <= end:
            mid = (end+start)/2
            print("start {}, end {}, mid {}".format(start, end, mid))
            if data[mid] == k:
                if  mid +1 <len(data) and data[mid+1] == k:
                    start = mid + 1
                else:
                    return mid
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1

print(Solution().GetNumberOfK([1,2,2,3], 2))
