class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        even_sum = n * (n + 1)
        odd_sum = n * n
        
        return math.gcd(even_sum, odd_sum)