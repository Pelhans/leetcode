/*************************************************************************
	> File Name: 53.cpp
	> Author: Pelhans
	> Mail: me@pelhans.com
	> Created Time: 2019年03月20日 星期三 17时32分28秒
 ************************************************************************/

#include<iostream>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = nums[0];
        int sum = 0;
        for(int i=0; i<nums.size(); i++){
            if(sum>=0){
                sum += nums[i];
            }
            else if(sum<0){
                sum = nums[i];
            }
            res = max(res, sum);
        }
        return res;
    }
    int max(int a, int b){
        if(a>b) return a;
        else return b;
    }
};

