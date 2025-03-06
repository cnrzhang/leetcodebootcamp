using namespace std;
#include <vector>

class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            int i = 0;
            int pre = 1;
            int post = 1;
            int n = nums.size();
            vector<int> answer(n, 1);
            for(i; i < n; i++){
                answer[i] *= pre;
                pre *= nums[i];
            }
            for(i = n - 1; i >= 0; i--){
                answer[i] *= post;
                post *= nums[i];
            }
    
            return answer;
    
        }
    };