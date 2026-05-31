class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=list(str(x))
        k=s[::-1]
        l=0
        while(l<len(s)):
            if s[l]!=k[l]:
                return False
            l+=1
        return True
            