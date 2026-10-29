class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        i = 0
        while i < len(nums):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
            i += 1
        return count