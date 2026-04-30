class Solution:
    def mirrorDistance(self, n: int) -> int:
        m=int(str(n)[::-1])
        return abs(n-m)