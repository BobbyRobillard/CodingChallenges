class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]

result = Solution().runningSum([1,2,3,4])
print(result)