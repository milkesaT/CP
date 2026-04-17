1from typing import List
2
3class Solution:
4    def pancakeSort(self, arr: List[int]) -> List[int]:
5        def reverse(nums, k):
6            left, right = 0, k - 1
7            while left < right:
8                nums[left], nums[right] = nums[right], nums[left]
9                left += 1
10                right -= 1
11        res = []
12        n = len(arr)
13
14        for size in range(n, 1, -1):
15            max_idx = arr.index(max(arr[:size]))
16
17            if max_idx != size - 1:
18                if max_idx != 0:
19                    reverse(arr, max_idx + 1)
20                    res.append(max_idx + 1)
21                reverse(arr, size)
22                res.append(size)
23        return res