class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0

        for sentence in sentences:
            count = 0
            for word in sentence.split():
                count += 1

            m = max(m, count)

        return m