#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def change(self, coins, amount):
        dp = [0] * (amount + 1)
        for i in range(1, amount+1):
            cost = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    cost = min(cost, dp[i-coin] + 1)
            dp[i] = cost
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]

# 40
print Solution().change([1,2,5], 200)
