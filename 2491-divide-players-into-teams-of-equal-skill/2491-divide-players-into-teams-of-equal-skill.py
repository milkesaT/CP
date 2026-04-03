class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        l=0
        r=n-1
        a=0
        target= skill[0] + skill[-1]
        while(l<r):
            s=skill[l]+skill[r]
            if(s!=target):
                return -1
            a+=skill[l]*skill[r]      
            l+=1
            r-=1
        return a
