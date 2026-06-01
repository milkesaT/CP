class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        s = [0] * n

        for i in range(n):
            start = max(0, i - nums[i])
            s[i] = prefix[i + 1] - prefix[start]
        return sum(s)