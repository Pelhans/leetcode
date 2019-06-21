#!/usr/bin/env python
# coding=utf-8

# 当 coin固定时的代码，即简单找零钱硬币最少版本
# 空间复杂度 O(1)
class Solution(object):
    def change(self, coins, amount):
        dp = [0] * (5)
        for i in range(1, amount + 1):
            res1 = res2 = res5 = float("inf")
            if i - 1 >= 0:
                res1 = dp[5-1]
            if i - 2 >= 0:
                res2 = dp[5-2]
            if i - 5 >= 0:
                res5 = dp[5-5]
            cost = min(res1, res2, res5) + 1
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = dp[3]
            dp[3] = dp[4]
            dp[4] = cost

        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]

# 40
print Solution().change([1,2,5], 200)

