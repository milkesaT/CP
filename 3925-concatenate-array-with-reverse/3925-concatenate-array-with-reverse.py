class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        r=[]
        for i in range(len(nums)):
            r.append(nums[len(nums)-1-i])
        return nums+r