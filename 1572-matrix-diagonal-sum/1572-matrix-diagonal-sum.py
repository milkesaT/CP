class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        c=0
        k=0
        row=len(mat)
        col=len(mat[0])-1

        for i in range(row):
            c+=mat[i][i]
            k+=mat[i][col-i]
            if i == col - i:
               k -= mat[i][col-i]
        return c+k