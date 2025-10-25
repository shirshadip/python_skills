class Solution:
    def totalMoney(self, n: int) -> int:
        week = n //7#number of complete weeks 
        rem = n %7 #number of remaining days
        print (week)
        print (rem)
a = Solution()
print (a.totalMoney(4))#10
print (a.totalMoney(10))#37
print (a.totalMoney(20))#96