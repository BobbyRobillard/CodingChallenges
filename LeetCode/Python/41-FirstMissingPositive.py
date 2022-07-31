class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        mapped_nums = {}
        for num in nums:
            mapped_nums[num] = num

        