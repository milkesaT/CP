class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        k=max(nums)
        l=min(nums)
        n = list(range(l, k+1))
        p=[]
        for i in n:
            if i not in nums:
               p.append(i)
        return p
