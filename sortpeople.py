class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n):
            minm=i
            for j in range(i+1,n):
                if(heights[i]<=heights[j]):
                      minm=j
            heights[i],heights[minm]=heights[minm],heights[i]
            names[i],names[minm]=names[minm],names[i]
        return names
                    
