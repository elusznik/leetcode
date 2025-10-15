class Solution:
    def countDigits(self, num: int) -> int:
        return sum(
            1
            for ch in str(num)
            if ch != "0" and num % int(ch) == 0
        )