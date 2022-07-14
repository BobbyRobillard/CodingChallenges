class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = -1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j] and i != j:
                    sliced = s[i:j]
                    if sliced:
                        print(sliced)
                    if sliced == sliced[::-1]:
                        longest = max(longest, len(sliced))
        return None


# -----------------------------------------------------------
#                           TESTING
# -----------------------------------------------------------

s = Solution()
results = [
    s.longestPalindrome("babad"),
    s.longestPalindrome("cbbd"),
]

for r in results:
    print(r)