class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n=set(sentence)
        if(len(n)==26):
            return True
        else:
            return False
