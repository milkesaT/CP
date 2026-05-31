class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        from collections import Counter
        
        l = list(str(n))
        count = Counter(l)
        
        r = 0
        for key, value in count.items():
            r += int(key) * value
        
        return r
         