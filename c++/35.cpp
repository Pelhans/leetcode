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
        int len_num = nums.size();
        while(len_num > 0){
            len_num /= 2;
            if (target == nums[len_num])
                return len_num;
            else if (target < nums[len_num]){
                if(nums.size() == 1)
                    return 0;
                if(target > nums[len_num-1]){
                    return len_num;
                }
                else{
                    std::vector<int>::const_iterator begin = nums.begin();
                    std::vector<int>::const_iterator end = nums.begin() + len_num-1;
                    std::vector<int> cut_vector(begin, end);
                    return searchInsert(cut_vector, target);
                }
                }
            else if (target > nums[len_num]){
                if (nums.size() <= 2)
                    return len_num + 1;
                if (target < nums[len_num+1]){
                    return len_num+1;
                }
                else{
                    std::vector<int>::const_iterator begin = nums.begin() + len_num + 1;
                    std::vector<int>::const_iterator end = nums.end();
                    std::vector<int> cut_vector(begin, end);
                    return len_num + 1 + searchInsert(cut_vector, target);
                }
            }
        }
    }
};
