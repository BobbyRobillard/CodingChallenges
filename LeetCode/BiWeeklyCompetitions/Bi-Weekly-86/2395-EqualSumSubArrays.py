class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        found_sums = {}
        for i in range(0, len(nums) - 1):
            curr_sum = nums[i] + nums[i+1]
            if curr_sum not in found_sums:
                found_sums[curr_sum] = True
            else:
                return True
        return False

s = Solution()
res = s.findSubarrays([4,2,4])
print(res)
res = s.findSubarrays([1,2,3,4,5])
print(res)
res = s.findSubarrays([0,0,0])
print(res)