#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        self.guibing(data)
        return self.count

    def guibing(self, array):
        if not array or len(array) == 1 :
            return array
        n = len(array)
        left = self.guibing(array[:n/2])
        right = self.guibing(array[n/2:])
        res = [0]*(len(left) + len(right))
        lp = len(left) - 1
        rp = len(right) - 1
        idx = len(left) + len(right) - 1
        while lp >=0 and rp >=0:
            if left[lp] > right[rp]:
                self.count += rp+1
                res[idx] = left[lp]
                idx -= 1
                lp -= 1
            else:
                res[idx] = right[rp]
                idx -= 1
                rp -= 1
        if lp+1 == 0:
            res[:rp+1] = right[:rp+1]
        else:
            res[:lp+1] = left[:lp+1]
        return res

a = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
b = [1, 2, 3, 4, 5, 6, 7, 0]
print Solution().InversePairs(a)
#print Solution().guibing([1,3,2,4])

