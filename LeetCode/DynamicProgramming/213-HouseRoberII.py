class Solution:
    def rob(self, nums: list[int]) -> int:
        def simple_rob(values):
            if not values: return 0
            prev1 = prev2 = 0
            for val in values:
                tmp = prev1
                prev1 = max(prev2 + val, prev1)
                prev2 = tmp
            return prev1

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))