class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
         ride=float("inf")
         for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                fland=landStartTime[i]+landDuration[i]
                startwater=max(fland,waterStartTime[j])
                total_land=startwater + waterDuration[j]
                
                fwater=waterStartTime[j]+waterDuration[j]
                startland=max(fwater,landStartTime[i])
                total_water=startland+landDuration[i]
                ride=min(ride,total_land,total_water)
         return ride
