class Solution:
    def getSneakyNumbers(self, nums) :
        seen = set()
        dup=[]
        for i in nums:

            if i in seen :
                dup.append(i)
            else :
                seen.add(i)
        return dup
sol = Solution()
n = [0,1,1,0]
print (sol.getSneakyNumbers(n))