class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        nar=[1]*n
        for l in range(k):
            for i in range(1,n):
                MOD = 10**9 + 7
                nar[i] = (nar[i-1] + nar[i]) % MOD
        return nar[n-1]

