class Solution:
    def countDigits(self, num: int) -> int:
        set = {}
        for digit in str(num):
            if num%int(digit)==0:
                if set.get(digit) is None:
                    set[digit] = 1
                else:
                    set[digit] += 1
        return sum(set.values())