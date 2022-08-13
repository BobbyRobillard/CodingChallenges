class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = [0] * 10001
        for el in nums:
            counts[el] += el
        
        prev1 = prev2 = 0
        for val in counts:
            tmp = prev1
            prev1 = max(prev2 + val, prev1)
            prev2 = tmp
        return prev1

s = Solution()
res = s.deleteAndEarn([3,4,2])
print(res)
res = s.deleteAndEarn([2,2,3,3,3,4])
print(res)