#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        if amount < 0 or len(coins) < 1:
            return 0
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount - coin + 1):
                dp[i+coin] += dp[i]
        return dp[amount]

print Solution().change(10, [1, 3, 5])

class Solution1(object):
    def change(self, coins, amount):
        dp = [[0]*(amount + 1)] * (len(coins) + 1)
        dp[0][0] = 1

        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(coins)][amount]

print Solution1().change([1, 3, 5], 10)

class Solution2(object):
    def change(self, coins, amount):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i-coin]

        return dp[amount]

print Solution().change(10, [1, 3, 5])
print Solution1().change([1, 3, 5], 10)
print Solution2().change([1, 3, 5], 10)
