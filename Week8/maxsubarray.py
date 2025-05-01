class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = -inf - 1
        currMax = 0 
        for i in range(len(nums)): 
            currMax += nums[i]
            globalMax = max(globalMax, currMax) 
            currMax = max(0, currMax)
        return globalMax  