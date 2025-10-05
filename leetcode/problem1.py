

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        

        seen = {}  # dictionary to store number:index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
    # Example usage:
result = Solution().twoSum([2,7,11,15], 9)
print(result)
result2 = Solution().twoSum([3,2,4], 6)
print(result2)
result3 = Solution().twoSum([3,3], 6)
print(result3)