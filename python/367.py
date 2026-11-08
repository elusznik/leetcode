class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == num:
                break
            elif mid * mid < num:
                start = mid + 1
            else:
                end = mid - 1
        return (mid * mid == num)