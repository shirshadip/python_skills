from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)  # sort descending
        for i in range(len(arr) - 2):
            if arr[i] < arr[i+1] + arr[i+2]:  # triangle condition
                return arr[i] + arr[i+1] + arr[i+2]
        return 0

    
print(Solution().largestPerimeter([2,1,2]))  # -> 5
print(Solution().largestPerimeter([1,2,1]))  # -> 0
print(Solution().largestPerimeter([3,2,3,4]))  # -> 10