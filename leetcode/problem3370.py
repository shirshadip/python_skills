class Solution:
    def smallestNumber(self, n):
        x = 1
        while x<n:
            x = (x<<1)|1 #shift left and filled with one 
        return x 
sol = Solution()
print(sol.smallestNumber(5))