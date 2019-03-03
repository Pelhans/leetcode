/*************************************************************************
	> File Name: 27.cpp
	> Author: 
	> Mail: 
	> Created Time: Sun 03 Mar 2019 03:31:38 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if(nums.size() == 0) return 0;
        int count = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != val){
                nums[count] = nums[i];
                count += 1;
            }
        }
        return count;
    }
};
