class Solution:
    def climbStairs(self, n: int) -> int:
        previous,current=0,1
        ways=0
        for _ in range(n):
            ways=previous+current
            previous=current
            current=ways
        return ways