class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=len(s)
        l=[]
        long=0
        for i in range(len(s)):
            if(s[i] not in l):
                l.append(s[i])
                long=max(long,len(l))
            else:
                while( s[i] in l):
                    del l[0]
                l.append(s[i])
        return(long)
          
     
