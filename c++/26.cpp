/*************************************************************************
	> File Name: 26.cpp
	> Author: 
	> Mail: 
	> Created Time: Sun 03 Mar 2019 03:22:53 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        int count = 0;
        for(int i=0; i < nums.size(); i++){
            if(nums[i] != nums[count]){
                nums[count+1] = nums[i];
                count += 1;
            }
        }
        return count + 1;
    }
};
