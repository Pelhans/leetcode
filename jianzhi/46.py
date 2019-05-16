#!/usr/bin/env python
# coding=utf-8

class Solution:
    def getTranslationCount(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number < 0:
            return 0
        str_num = str(number)
        dp = {}
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(str_num)+1):
            two_digit = int(str_num[i-2]+str_num[i-1])
            if two_digit > 25:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp.values()[-1]

if __name__=="__main__":
    print(Solution().getTranslationCount(12258))
    print(Solution().getTranslationCount(12319))
    print(Solution().getTranslationCount(-3))
    print(Solution().getTranslationCount(0))
    print(Solution().getTranslationCount(5))

