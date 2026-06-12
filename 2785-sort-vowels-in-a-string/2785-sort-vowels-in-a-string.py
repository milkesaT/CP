class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        # Extract vowels
        arr = [ch for ch in s if ch in vowels]
        # Sort vowels by ASCII value
        arr.sort()
        res = []
        j = 0
        for ch in s:
            if ch in vowels:
                res.append(arr[j])
                j += 1
            else:
                res.append(ch)
        
        return "".join(res)