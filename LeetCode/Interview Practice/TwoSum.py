# O(n^2), brute force approach
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i, val1 in enumerate(nums):
#             for j, val2 in enumerate(nums):
#                 if val1 + val2 == target and i != j:
#                     return [i, j]
#         pass
# s = Solution()
# print(s.twoSum([2,7,11,15], 9))

# O(n), two-pass hash-table approach
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 
s = Solution()
print(s.twoSum([2,7,11,15], 9))