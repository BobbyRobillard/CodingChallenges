"""
Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.
"""
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        # Check edge case
        if 0 not in nums:
            return 0
        # Go through the entire array until encountering a zero
        num_subarrays = 0
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            # When a zero is found, check if there are any zeros to add to subarray
            if nums[i] == 0:
                num_subarrays += 1 # Add one for new single zero
                j = i + 1
                extra = 0
                while j < len_nums and nums[j] == 0:
                    extra += 1
                    num_subarrays += 1 # Add one for new single zero
                    num_subarrays += extra # Add extra for each possible extra subarray
                    j += 1
                i = j
            else:
                i += 1
        return num_subarrays

s = Solution()
res = s.zeroFilledSubarray([1,3,0,0,2,0,0,4])
print(res)
res = s.zeroFilledSubarray([0,0,0,2,0,0])
print(res)
res = s.zeroFilledSubarray([2,10,2019])
print(res)