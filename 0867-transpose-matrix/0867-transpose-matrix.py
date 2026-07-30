class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ma = []
        row=len(matrix)
        col=len(matrix[0])
        for i in range(col):
            r = []
            for j in range(row):
                r.append(matrix[j][i])
            ma.append(r)
        return ma
