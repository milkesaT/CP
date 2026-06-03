from bisect import bisect_right
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        from bisect import bisect_right
        water = sorted(zip(waterStartTime, waterDuration))
        ws = [x[0] for x in water]
        wd = [x[1] for x in water]

        m = len(water)

        # prefix min of water duration
        prefDur = [0] * m
        prefDur[0] = wd[0]

        for i in range(1, m):
            prefDur[i] = min(prefDur[i - 1], wd[i])

        # suffix min of waterStart + waterDuration
        suffFinish = [0] * m
        suffFinish[-1] = ws[-1] + wd[-1]

        for i in range(m - 2, -1, -1):
            suffFinish[i] = min(
                suffFinish[i + 1],
                ws[i] + wd[i]
            )

        ans = float("inf")

        # land to water
        for ls, ld in zip(landStartTime, landDuration):

            landFinish = ls + ld

            idx = bisect_right(ws, landFinish)

            # water already opened
            if idx > 0:
                ans = min(ans,
                          landFinish + prefDur[idx - 1])

            # water opens later
            if idx < m:
                ans = min(ans,
                          suffFinish[idx])
        land = sorted(zip(landStartTime, landDuration))
        ls = [x[0] for x in land]
        ld = [x[1] for x in land]
        n = len(land)
        prefDur = [0] * n
        prefDur[0] = ld[0]
        for i in range(1, n):
            prefDur[i] = min(prefDur[i - 1], ld[i])
        suffFinish = [0] * n
        suffFinish[-1] = ls[-1] + ld[-1]
        for i in range(n - 2, -1, -1):
            suffFinish[i] = min(
                suffFinish[i + 1],
                ls[i] + ld[i]
            )
        for ws_, wd_ in zip(waterStartTime, waterDuration):
            waterFinish = ws_ + wd_
            idx = bisect_right(ls, waterFinish)
            # land already opened
            if idx > 0:
                ans = min(ans,
                          waterFinish + prefDur[idx - 1])

            # land opens later
            if idx < n:
                ans = min(ans,
                          suffFinish[idx])
        return ans