1class Solution:
2    def reverseDegree(self, s: str) -> int:
3        m=0
4        letters = string.ascii_lowercase
5        for i in range(len(s)):
6            value = 26 - letters.index(s[i])
7            m+=value*(i+1)
8        return m
9