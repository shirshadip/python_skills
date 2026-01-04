from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            divisors = set()

            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)

                # Early stop if more than 4 divisors
                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                total += sum(divisors)

        return total



print(Solution().sumFourDivisors([21, 21]))
print(Solution().sumFourDivisors([21,4,7]))
