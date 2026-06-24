class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        s=[]
        while l<r:
            s.append(sum([nums[l], nums[r]]))
            l+=1
            r-=1
        return max(s)

