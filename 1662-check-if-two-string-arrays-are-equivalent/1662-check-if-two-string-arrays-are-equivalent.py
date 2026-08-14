class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        c="".join(word1)
        d="".join(word2)
        if c==d:
            return True
        else:
            return False