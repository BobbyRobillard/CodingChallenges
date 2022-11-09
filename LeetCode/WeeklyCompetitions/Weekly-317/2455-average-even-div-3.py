import math

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        matched = [x for x in nums if x % 3 == 0 and x % 2 == 0]
        return math.floor(sum(matched) / len(matched)) if matched else 0