class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        s = []

        for x in nums:
            if x >= 0:
                p.append(x)
            else:
                n.append(x)

        for i in range(len(p)):
            s.append(p[i])
            s.append(n[i])

        return s