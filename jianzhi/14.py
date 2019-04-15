#!/usr/bin/env python
# coding=utf-8

class Solution:
    def MaxProductAfterCut(self, n):
        if n < 2:
            return 0
        products = [0]*(n+1)
        if n == 2:
            return 1
        if n == 3:
            return 2

        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        for i in range(4, n+1):
            max = 0
            for j in range(1, i/2+1):
                product = products[j]*products[i-j]
                if product > max:
                    max = product
            products[i] = max
        return products[n]

if __name__ == "__main__":
    print(Solution().MaxProductAfterCut(8))
