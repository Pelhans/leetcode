/*************************************************************************
	> File Name: 35.cpp
	> Author: 
	> Mail: 
	> Created Time: Mon 04 Mar 2019 09:41:29 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size();
        while(low < high){
            int mid = low + (high-low)/2;
            if(nums[mid] > target) high = mid;
            else if (nums[mid] < target) low = mid+1;
            else return mid;
        }
        return low;
    }
};
