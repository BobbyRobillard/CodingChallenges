class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = {}
        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                return c


s = Solution()
res = s.repeatedCharacter("abccbaacz")
print(res)
res = s.repeatedCharacter("abcdd")
print(res)