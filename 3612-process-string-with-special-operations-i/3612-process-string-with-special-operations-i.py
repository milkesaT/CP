class Solution:
    def processStr(self, s: str) -> str:
        result=[]
        for i in s:
            if i.isalpha():
                result.append(i)
            if i == "*" and result:
                result.pop()
            if i=="%":
                result.reverse()
            if i=="#":
                result=result*2
        r="".join(result)
        return r