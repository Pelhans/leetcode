/*************************************************************************
	> File Name: c++/66.cpp
	> Author: Pelhans
	> Mail: me@pelhans.com
	> Created Time: Wed 20 Mar 2019 08:59:53 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len=digits.size();
        digits[len-1]++;
        for(int i=len-1;i>=0;i--){
            if(digits[0]==10){
            digits[0]=0;
            digits.insert(digits.begin(),1);
            }
            else if(digits[i]==10){
                digits[i]=0;
                digits[i-1]++;
            }           
        }
        return digits;
    }
};
