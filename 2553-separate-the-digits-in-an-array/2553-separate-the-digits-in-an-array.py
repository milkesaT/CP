class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        s = "".join(map(str, nums))
        for i in s:
            l.append(i)
        return list(map(int,l))
