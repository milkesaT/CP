class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = "".join(c for c in s if c.isalnum())  # Keeps only letters and numbers
        k=k.lower()
        if k==k[::-1] :
            return True
        return False
        