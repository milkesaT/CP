class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        r=max(nums)-min(nums)
        return k*r