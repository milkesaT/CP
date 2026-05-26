class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for ch in set(word.lower()):
            if ch.upper() in word and ch.lower() in word:
                count += 1

        return count