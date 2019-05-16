#!/usr/bin/env python
# coding=utf-8

class Solution:
    #假设输入array为一维数组，行数为rows,列数为cols,要求输出为最大的那个数值
    def getMaxValue1(self,array,rows,cols):
        # write code here
        if len(array) == 0 or rows <= 0 or cols <= 0:
            return 0
        maxValue = [[0 for i in range(cols)] for i in range(rows)]
        for c in range(cols):
            for r in range(rows):
                up = 0
                left = 0
                if r > 0:
                    up = maxValue[r-1][c]
                if c > 0:
                    left = maxValue[r][c-1]
                maxValue[r][c] = max(up, left) + array[r*cols+c]
        return maxValue[rows-1][cols-1]

if __name__=="__main__":
    print(Solution().getMaxValue1([1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5],4,4))
    print(Solution().getMaxValue1([15], 1, 1))
    print(Solution().getMaxValue1([1,10,3,8], 1, 4))
    print(Solution().getMaxValue1([1, 10, 3, 8], 4, 1))
    print(Solution().getMaxValue1([],5,5))
