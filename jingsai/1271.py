#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        neg = defaultdict(list)
        zeros = defaultdict(list)
        pos = defaultdict(list)
        for i,j in enumerate(A):
            if j > 0:
                pos[j].append(i)
            elif j == 0:
                zeros[j].append(i)
            elif j < 0:
                neg[j].append(i)
        for i in range(K):
            if len(neg) != 0:
                sn = list(neg.keys())
                sn.sort()
                A[neg[sn[0]][0]] = -A[neg[sn[0]][0]]
                pos[A[neg[sn[0]][0]]].append(neg[sn[0]][0])
                neg[sn[0]].pop(0)
                if len(neg[sn[0]]) == 0:
                    neg.pop(sn[0])
            elif len(zeros) != 0:
                continue
            elif len(pos) != 0:
                print "here?", pos
                sp = list(pos.keys())
                sp.sort()
                A[pos[sp[0]][0]] = -A[pos[sp[0]][0]]
                neg[A[pos[sp[0]][0]]].append(pos[sp[0]][0])
                pos[sp[0]].pop(0)
                if len(pos[sp[0]]) == 0:
                    pos.pop(sp[0])
        return sum(A)

