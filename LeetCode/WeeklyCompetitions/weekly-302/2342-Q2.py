"""
2342. Max Sum of a Pair With Equal Sum of Digits
You are given a 0-indexed array nums consisting of positive integers. 
You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
"""

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        # Calculate the digit sum of each item, store in hashmap
        sums = {}
        for item in nums:
            digits_sum = sum(map(int, "".join(str(item))))
            if digits_sum in sums:
                sums[digits_sum].append(item)
            else:
                sums[digits_sum] = [item]

        max_sum = -1
        for key in sums:
            if len(sums[key]) >= 2:
                sums[key].sort()
                max_sum = max(max_sum, sum(sums[key][-2:]))
        return max_sum

s = Solution()
res = s.maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401])
print(res)