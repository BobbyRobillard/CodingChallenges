class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # Store number of operations
        count = 0
        # While each item is not zero
        while any(x!=0 for x in nums):
            # Find the current smallest element
            min_num = min([x for x in nums if x > 0])
            # Subtract min_num from each non-zero element of nums
            nums = [x - min_num for x in nums if x > 0]
            count += 1
        return count

s = Solution()
res = s.minimumOperations([1,5,0,3,5])
print(res)
res = s.minimumOperations([0])
print(res)