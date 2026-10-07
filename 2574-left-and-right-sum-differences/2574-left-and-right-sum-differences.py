class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightsum=[]
        for i in range(len(nums)):
            left = sum(nums[:i])
            leftSum.append(left)
            right=sum(nums[i+1:])
            rightsum.append(right)
        an=[]
        for i in range(len(nums)):  
            an.append(abs(leftSum[i]-rightsum[i]))
        return an