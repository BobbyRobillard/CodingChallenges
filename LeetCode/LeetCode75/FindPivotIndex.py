# -----------------------------------------------------------
#                         PROMPT
# -----------------------------------------------------------

# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# -----------------------------------------------------------
#            NAIVE SOLUTION | calcs. right side too
# -----------------------------------------------------------

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if 0 == sum(nums[1:]): return 0
        for i in range(1, len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

# -----------------------------------------------------------
#            BETTER SOLUTION | only calcs. left side
# -----------------------------------------------------------
# 193 ms | 15.2 MB

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, val in enumerate(nums):
            if left_sum == (total_sum - left_sum - val):
                return i
            left_sum += val
        return -1


# -----------------------------------------------------------
#                           TESTING
# -----------------------------------------------------------

s = Solution()
results = [
    s.pivotIndex([1,7,3,6,5,6]),
    s.pivotIndex([1,2,3]),
    s.pivotIndex([2,1,-1]),
]

for r in results:
    print(r)