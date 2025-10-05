import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root=math.sqrt(num)

        if root!=int(root):
            return False
        elif root*root==num:
            return True
sol=Solution()
print(sol.isPerfectSquare(16))  # Output: True
print(sol.isPerfectSquare(14))  # Output: False