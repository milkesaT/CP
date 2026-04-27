class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        s = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for keys, value in d.items():
            if value == 2:
                s.append(keys)
        return s
