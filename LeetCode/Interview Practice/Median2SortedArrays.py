# -----------------------------------------------------------
#                         PROMPT
# -----------------------------------------------------------

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# -----------------------------------------------------------

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new_lst = sorted(nums1 + nums2)
        lst_len = len(new_lst)
        return new_lst[lst_len//2] if lst_len % 2 != 0 else (new_lst[lst_len//2 - 1] + new_lst[(lst_len//2)]) / 2

# -----------------------------------------------------------
#                         TESTING
# -----------------------------------------------------------

s = Solution()
results = [
    s.findMedianSortedArrays([1,3], [2]),
    s.findMedianSortedArrays([1,2], [3,4])
]

for result in results:
    print(result)