import math
class Solution:
    def fillCups(self, amounts: list[int]) -> int:
        mx = max(amounts)
        mx_index = amounts.index(mx)
        remaining_sum = sum(amounts[:mx_index] + amounts[mx_index+1:])
        return mx if remaining_sum <= mx else mx + math.ceil((remaining_sum - mx) / 2)

s = Solution()
res = s.fillCups([1,4,2])
print(res)
res = s.fillCups([5,4,4])
print(res)
res = s.fillCups([5,0,0])
print(res)
res = s.fillCups([0,4,5])
print(res)