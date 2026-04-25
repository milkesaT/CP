class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False

       # return not stack
        if(len(stack)==0):
            return True
        else:
            return False