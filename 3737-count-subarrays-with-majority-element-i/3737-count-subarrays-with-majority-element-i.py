from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            freq = 0

            for j in range(i, n):

                if nums[j] == target:
                    freq += 1

                length = j - i + 1

                if freq > length // 2:
                    count += 1

        return count