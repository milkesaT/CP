class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        distinct = 0
        for i in arr:
            if count[i] == 1:
                distinct += 1
                if distinct == k:
                    return i
        return ""