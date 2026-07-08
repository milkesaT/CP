class Solution:
    def sumAndMultiply(self, n: int) -> int:
        k = [i for i in str(n) if i != '0']

        if not k:
            return 0

        o = sum(int(i) for i in k)
        l = int(''.join(k))

        return l * o