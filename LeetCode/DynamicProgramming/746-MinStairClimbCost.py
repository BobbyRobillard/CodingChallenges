class Solution:

    def minCostClimbingStairs(self, costs):
        for i in range(2, len(costs)):
            costs[i] += min(costs[i-1], costs[i-2])
        return min(costs[-1], costs[-2])

    def minCostClimbingStairs2(self, costs: list[int]) -> int:
        n = len(costs)
        dp = {
            n: 0,
            n-1: costs[n-1],
            n-2: costs[n-2]
        }
        for i in range(n - 2, -1, -1):
            dp[i] = costs[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])

res = Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
print(res)