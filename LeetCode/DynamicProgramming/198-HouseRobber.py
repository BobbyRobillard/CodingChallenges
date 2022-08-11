class Solution:
    # Bottom-Up Memoized DP Solution
    def rob(self, values):
        if not values:
            return 0
        if len(values) == 1:
            return values[0]

        memo = [0] * (len(values))
        memo[0] = values[0]
        memo[1] = max(values[0], values[1])

        for i in range(2, len(values)):
            memo[i] = max(memo[i-1], memo[i-2] + values[i])

        return memo[len(values) - 1]

    # Iterative variable driven solution, dervied from DP and recursive relations
    def rob2(self, values):
        if not values: return 0
        prev1 = prev2 = 0
        for val in values:
            tmp = prev1
            prev1 = max(prev2 + val, prev1)
            prev2 = tmp
        return prev1

s = Solution()
res = s.rob2([1,2,3,1])
print(res)