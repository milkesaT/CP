class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s=set(nums)
        # if len(s)!=len(nums):
        #     return True
        # else:
        #     return False
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False