class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #a=[]
        count=0
        countl=0

        for i in nums1:
            if i in nums2:
                count+=1
        for i in nums2:
            if i in nums1:
                countl+=1
        a=[count,countl]
        return a
