class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for ch in set(word.lower()):
            if ch in word and ch.upper() in word:
                if word.rindex(ch) < word.index(ch.upper()):
                    count += 1
        return count