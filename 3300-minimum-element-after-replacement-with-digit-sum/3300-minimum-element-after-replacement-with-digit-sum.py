class Solution:
    def minElement(self, nums: List[int]) -> int:
        s = []
        for i in range(len(nums)):
               s.append(sum(map(int, str(nums[i]))))

        return min(s)