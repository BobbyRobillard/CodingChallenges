class Solution:
    def longestOnes(self, arr, k):
        count = 0
        for j in range(len(arr)):
            k -= 1 - arr[j]
            if k < 0:
                k += 1 - arr[count]
                count += 1
        return j - count + 1

    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks = list(map(lambda x: 1 if x == "B" else 0, list(blocks)))
        for i in range(10000):
            res = self.longestOnes(blocks, i)
            if res >= k:
                return i
        return -1

s = Solution()
print(s.minimumRecolors("WBBWWBBWBW", 7))
print(s.minimumRecolors("WBWBBBW", 2))
