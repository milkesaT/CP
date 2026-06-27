class Solution:
    def interpret(self, command: str) -> str:
        com=[]
        for i in command:
            if i=="G":
                com.append(i)
            if i=="(":
                com.append("o")
            if i=="a":
                com.pop()
                com.append("al")
        return "".join(com)