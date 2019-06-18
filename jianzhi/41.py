#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
 
class Solution:
    def __init__(self):
        self.minNums=[]
        self.maxNums=[]
    def maxHeapInsert(self,num):
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:
            if self.maxNums[i] > self.maxNums[(i - 1) / 2]:
                t = self.maxNums[(i - 1) / 2]
                self.maxNums[(i - 1) / 2] = self.maxNums[i]
                self.maxNums[i] = t
                i = (i - 1) / 2
            else:
                break
    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti + 1] > self.maxNums[nexti]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                tmp = self.maxNums[i]
                self.maxNums[i] = self.maxNums[nexti]
                self.maxNums[nexti] = tmp
                i = nexti
            else:
                break
        return  t
    def minHeapInsert(self,num):
        self.minNums.append(num)
        lens = len(self.minNums)
        i = lens - 1
        while i > 0:
            if self.minNums[i] < self.minNums[(i - 1) / 2]:
                t = self.minNums[(i - 1) / 2]
                self.minNums[(i - 1) / 2] = self.minNums[i]
                self.minNums[i] = t
                i = (i - 1) / 2
            else:
                break
    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[nexti] < self.minNums[i]:
                tmp = self.minNums[i]
                self.minNums[i] = self.minNums[nexti]
                self.minNums[nexti] = tmp
                i = nexti
            else:
                break
        return t
    def Insert(self, num):
        if (len(self.minNums)+len(self.maxNums))&1==0:
            if len(self.maxNums)>0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
        else:
            if len(self.minNums)>0 and num > self.minNums[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)
    def GetMedian(self,n=None):
        allLen = len(self.minNums) + len(self.maxNums)
        if allLen ==0:
            return -1
        if allLen &1==1:
            return self.minNums[0]
        else:
            return (self.maxNums[0] + self.minNums[0]+0.0)/2
