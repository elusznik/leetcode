class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = 0, 0
        for price in cost:
            prev, curr = curr, price + min(prev, curr)
        return min(prev, curr)