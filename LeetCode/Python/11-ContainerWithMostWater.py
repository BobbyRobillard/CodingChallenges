class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i = 0
        j = len(heights) - 1
        curr_max = -1
        while i < j:
            curr_max = max(curr_max, (j-i) * (min(heights[i], heights[j])))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return curr_max

s = Solution()
print(s.maxArea([1,1,8,1,8,100,100]))