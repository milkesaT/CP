class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r=0
        sum_nums=[]
        for i in range(len(nums)):
            r += nums[i]
            sum_nums.append(r)
        return sum_nums