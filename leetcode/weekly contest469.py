from typing import List
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        comp= []
        power = 1
        while n> 0:
            dig = int(n % 10)
            if dig !=0:
                comp.append (int(dig * power))
            n //=10
            power *=10
        return comp[::-1]
print(Solution().decimalRepresentation(239))   # -> [200, 30, 9]
print(Solution().decimalRepresentation(5009))  # -> [5000, 9]
print(Solution().decimalRepresentation(7))  # -> [7]