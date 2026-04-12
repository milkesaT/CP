class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        if(k==0):
            return res
        for i in range(n):
                total_sum=0
                if(k>0):
                    for j in range(1,k+1):
                        total_sum+=code[(i+j)%n]
                else:
                    for j in range(1,abs(k)+1):
                        total_sum+=code[(i-j)%n]
                res[i]=total_sum
        return res
