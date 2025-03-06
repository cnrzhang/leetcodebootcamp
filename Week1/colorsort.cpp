using namespace std;

#include <vector>

class Solution {
    public:
        void sortColors(vector<int>& nums) {
            int n = nums.size();
            int low = 0, high = n - 1, mid = 0;
            while( high >= mid){
                if(nums[mid] == 0){ // case 1, we leave in place and proceed to next 
                    swap(nums[low], nums[mid]);
                    mid++;
                    low++;
                }
                else if(nums[mid] == 1){ //case 2, we increase by 1 but leave low behind
                        mid++;
                    }
                    else{//case 3, we move it to the end of the array, then decrement high by one
                        swap(nums[mid], nums[high]);
                        high--;
                    }
            
        }
        }
    };