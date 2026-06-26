from bisect import bisect_left, insort
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # target -> +1
        # others -> -1
        # Then we need subarrays with sum > 0
        prefix = 0
        sorted_prefix = [0]
        count = 0
        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1
            # Count previous prefix sums < current prefix
            count += bisect_left(sorted_prefix, prefix)
            # Insert current prefix while keeping list sorted
            insort(sorted_prefix, prefix)

        return count