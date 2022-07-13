# Naive approach, sums everything at each step
# 102 ms | 14.1 MB
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]

result = Solution().runningSum([1,2,3,4])
print(result)
# ----------------------------------------------------------
# Better approach, store previous sum values
# 51 ms	| 14.2 MB
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[i-1] + nums[i])
        return sums
# -----------------------------------------------------------
# Different approach, does everything in place, not as good on time though.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
# -----------------------------------------------------------
result = Solution().runningSum([1,2,3,4])
print(result)