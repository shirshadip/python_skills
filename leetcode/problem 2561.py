#2561. Rearranging Fruits
from collections import Counter

class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        total = Counter(basket1) + Counter(basket2)

        # Step 1: Check if it's possible to equalize
        for v in total.values():
            if v % 2 != 0:
                return -1

        # Step 2: Count excess fruits
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        excess = []

        for fruit in total:
            diff = count1[fruit] - total[fruit] // 2
            if diff > 0:
                excess.extend([fruit] * diff)
            elif diff < 0:
                excess.extend([fruit] * (-diff))

        # Only need to handle half (each swap fixes 2 items)
        excess.sort()
        half = len(excess) // 2

        # Find the globally smallest fruit value
        min_fruit = min(total)

        # Step 3: Calculate minimum cost
        cost = 0
        for i in range(half):
            cost += min(excess[i], 2 * min_fruit)

        return cost

# \U0001f9ea Sample Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    basket1 = [4, 2, 2, 2]
    basket2 = [1, 4, 1, 2]
    print("Output 1:", sol.minCost(basket1, basket2))  # Expected: 1

    # Test Case 2
    basket1 = [2, 3, 4, 1]
    basket2 = [3, 2, 5, 1]
    print("Output 2:", sol.minCost(basket1, basket2))  # Expected: -1