#!/usr/bin/env python
# coding=utf-8

#coding=utf8
def get_ans(n):
    dp = [[0 for i in range(6*n)] for i in range(n)]
 
    for i in range(6):
        dp[0][i] = 1
    # print dp
    for i in range(1,n):
        for j in range(i,6*(i+1)):
            dp[i][j] = dp[i-1][j-6] + dp[i-1][j-5] +dp[i-1][j-4]+\
                            dp[i - 1][j - 3] +dp[i-1][j-2] +dp[i-1][j-1]
 
    count = dp[n-1]
    return count
 
print get_ans(2)
