class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total = sum(nums)
        single = sum(n for n in nums if n < 10)
        return total != 2 * single