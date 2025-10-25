class Solution:
    def totalMoney(self, n: int) -> int:
        week = n //7#number of complete weeks 
        rem = n %7 #number of remaining days
        
        total_full_weeks = 28 * week + 7 * week * (week - 1) // 2
        total_remaining = rem * (week + 1) + rem * (rem - 1) // 2
        
        return total_full_weeks + total_remaining
a = Solution()
print (a.totalMoney(4))#10
print (a.totalMoney(10))#37
print (a.totalMoney(20))#96