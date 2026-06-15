class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int: 
        n = len(arr)
        total = 0
        for i in range(n):         
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                if (j - i + 1) % 2 == 1:
                    total += curr_sum

        return total