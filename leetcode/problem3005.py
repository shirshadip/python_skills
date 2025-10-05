from collections import Counter
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        total=0
        freq = Counter(nums)
        max_freq = max(freq.values())
        for i in range(max_freq):
            count = sum(1 for v in freq.values() if v > i)
            total = max(total, count)

        return total

sol = Solution()
print (sol.maxFrequencyElements([1,2,2,3,1,4,4,4]))  # Output: 3
print (sol.maxFrequencyElements([1,1,1,2,2,3]))  # Output: 3
print (sol.maxFrequencyElements([1,2,3,4,5]))  #    Output: 5