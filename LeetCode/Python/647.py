class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(2):
                left = i
                right = left + j

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
        return ans

s = Solution()
res = s.countSubstrings("aaa")
print(res)