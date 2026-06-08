class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=3
        count=0
        for i in range(0,len(s)-k+1):
            sub=s[i:i+k]
            if len(set(sub))==k:
                count+=1
        return count



            