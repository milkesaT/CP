class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        max_sum = s
        for i in range(k, len(nums)):
            s += nums[i]      
            s -= nums[i - k]    
            max_sum = max(max_sum, s)
        return max_sum / k
