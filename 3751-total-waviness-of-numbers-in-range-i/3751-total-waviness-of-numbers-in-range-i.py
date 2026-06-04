class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for num in range(num1, num2 + 1):
            digits = [int(d) for d in str(num)]
            for i in range(1, len(digits) - 1):
                # peak
                if digits[i] > digits[i - 1] and digits[i] > digits[i + 1]:
                    count += 1
                # valley
                elif digits[i] < digits[i - 1] and digits[i] < digits[i + 1]:
                    count += 1
        return count