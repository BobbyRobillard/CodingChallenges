class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 1000000007
        dp = [1, 2]
        for i in range(2, n+1):
            dp.append((dp[i-1] + dp[i-2]) % mod)
        return (dp[n] * dp[n]) % mod


s = Solution()
res = s.countHousePlacements(1)
print(res)
res = s.countHousePlacements(2)
print(res)