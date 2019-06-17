#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        if len(data)<=0:
            return 0
        if len(data) == 1:
            return data
        print "rank result: ", self.guibing(data)
        return self.count
        
    def guibing(self, data):
        if len(data) == 1:
            return 0, data
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        
        l1 = self.guibing(left)
        r1 = self.guibing(right)
        result = self.merge(l1[1], r1[1])
        print "result: ", result
        self.count += result[0]
        return result[1]
    
    def merge(self, left, right):
        if not left or not right:
            return left + right
        result = [0] * (len(left) + len(right))
        count = 0
        i = len(left) + len(right) - 1
        while len(right) > 0 and len(left) > 0:
            if left[-1] >= right[-1]:
                count += len(right)
#                print "count? ", count
                result[i] = left.pop()
            else:
                result[i] = right.pop()
            i -= 1

        result[:len(left)] = left
        result[:len(right)] = right
#        count += len(right)
        print "count? ", count
        return count, result

#a = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
#print Solution().InversePairs(a)

print Solution().guibing([  1,2,3,4,5,6,7,0 ])
