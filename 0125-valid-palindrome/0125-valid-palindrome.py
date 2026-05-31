class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())

        lst = list(s)
        lst2 = lst[::-1]

        l = 0
        while l < len(lst):
            if lst[l] != lst2[l]:
                return False
            l += 1

        return True