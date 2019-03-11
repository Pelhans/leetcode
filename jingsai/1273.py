#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        from collections import Counter
        order = Counter(A + B)
        order = order.most_common(len(order.keys()))
        if order[0][1] < len(A):
            return -1
        min_top = 0
        min_bot = 0
        C = A
        D = B
        for k, _ in order:
            for i, j in enumerate(A):
                if k == A[i] and k != B[i]:
                    min_bot += 1
                    D[i] = A[i]
                elif k == B[i] and k != A[i]:
                    min_top += 1
                    C[i] = B[i]
                elif k == A[i] and k == B[i]:
                    continue
                elif k != A[i] and k != B[i]:
                    min_top = 0
                    min_bot = 0
                    C = A
                    D = B
                    break
            if len(set(C)) == 1 or len(set(D)) == 1:
                return min(min_top, min_bot)
        return -1
            

