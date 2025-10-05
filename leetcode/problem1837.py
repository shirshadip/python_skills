class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total =0
        while n>0:
            a= n%k
            b =n//k
            c = str(a)
            d = str(b)
            total+=int(c)
            n=b

        return total

sol = Solution()
print (sol.sumBase(34,6))
print (sol.sumBase(10,10))