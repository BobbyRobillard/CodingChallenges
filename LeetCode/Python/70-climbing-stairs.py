class Solution:
    def climbStairs(self, n: int) -> int:
        res = {
            0: 0, 1: 1, 2: 2
        }
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]