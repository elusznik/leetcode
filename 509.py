class Solution:
    def fib(self, n: int) -> int:
        a, b = 1, 0
        for _ in range(n): a, b = b, b+a
        return b