#include <vector>
using namespace std;



class Solution {
    public:
        vector<int> twoSum(vector<int>& numbers, int target) {
            int i = 0;
            int j = numbers.size() - 1;
            vector<int> ans(2);
            while(i<j){
                int test = numbers[i] + numbers[j];
                if(test == target){
                    ans = {i+1, j+1};
                    break;
                }
                else if(test>target){
                    j--;
                }
                else{
                    i++;
                }
            }
            
            return ans;
        }
    };