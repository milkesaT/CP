class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s=[]
        for i in order:
            if i in friends:
                s.append(i)
        return s