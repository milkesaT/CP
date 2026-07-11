class Solution:
    def countBits(self, n: int) -> List[int]:
        s=[]
        for i in range(n+1):
            binary=bin(i)[2:]
            s.append(sum(map(int, binary)))
        return s