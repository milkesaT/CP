class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort
        m=1000
        for i in range(len(nums)):
            m=min(m,nums[i])
        return m