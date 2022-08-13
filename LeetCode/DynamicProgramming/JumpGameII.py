class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            j = i
            while j <= (i + nums[i]) and j < n:
                dp[j] = min(dp[j], dp[i]+1)
                j += 1
        return dp[n-1]