class Solution:
    def canJump(self, nums):
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            for j in range(i+1, min(n, i+nums[i]+1)):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]

#     def canJump3(self, nums: List[int]) -> bool:
#         n = len(nums)
#         maxPos = 0
#         i = 0
#         while i <= maxPos:
#             maxPos = max(maxPos, i + nums[i])
#             if maxPos >= n - 1: return True
#             i += 1
        
#         return False


s = Solution()
res = s.canJump([0,1,3])
print(res)
res = s.canJump([2,3,1,1,4])
print(res)