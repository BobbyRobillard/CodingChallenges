class Solution:
    def fib(self, n: int) -> int:
        res = {
            0: 0,
            1: 1
        }
        if n < 2:
            return res[n]
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[n-1] + res[n-2]


s = Solution()
print(s.fib(3))