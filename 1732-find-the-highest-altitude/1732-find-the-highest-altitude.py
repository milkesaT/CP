class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h=0
        he=0
        for i in gain:
            h+=i
            he=max(he,h)
        return he
