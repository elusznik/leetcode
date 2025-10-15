class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = sum(number for number in nums if number<=9)
        double = sum(number for number in nums if number>=10)
        return (single>double) or (double>single)