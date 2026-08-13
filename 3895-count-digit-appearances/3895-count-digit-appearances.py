class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for k in nums:
            for d in str(k):
                if int(d) == digit:
                    count += 1

        return count