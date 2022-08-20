class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        def maxSubArray(nums):
            dp = [0 for i in range(len(nums))]
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                dp[i] = max(dp[i-1]+nums[i],nums[i])
            return max(dp)
        # Find max subarray in each of the inputs
        max_n1 = maxSubArray(nums1)
        max_n2 = maxSubArray(nums2)
        # Get current sums
        sum_n1 = sum(nums1)
        sum_n2 = sum(nums2)
        # Check if swapping each subarray in either will give new max
        possible_solutions = [sum_n1, sum_n2, sum_n1 - max]
