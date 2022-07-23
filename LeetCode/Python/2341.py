"""
Input: nums = [1,3,2,1,3,2,2]
Output: [3,1]
"""
from collections import Counter

class Solution:
    # Solution 1) Use Recursion
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        n_len = len(nums)
        def helper(remaining, pairs):
            if not remaining: return pairs
            temp = remaining[0]
            if temp in remaining[1:]:
                remaining.remove(temp)
                remaining.remove(temp)
                return helper(remaining, pairs + 1)
            else:
                remaining.remove(temp)
                return helper(remaining, pairs)
        pairs = helper(nums, 0)
        return [pairs, n_len - pairs * 2]

    # Solution 2) Use Hashmap
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        s = Counter(nums)
        pairs = singles = 0
        for key in s.keys():
            pairs += s[key] // 2
            singles += s[key] % 2
        return [pairs, singles]


s = Solution()
res = s.numberOfPairs([1,3,2,1,3,2,2])
print(res)
res = s.numberOfPairs([1,1])
print(res)
res = s.numberOfPairs([0])
print(res)