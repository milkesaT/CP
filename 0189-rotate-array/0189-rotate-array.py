class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        rotated = nums[-k:] + nums[:-k] 
        for i in range(n):
            nums[i] = rotated[i]