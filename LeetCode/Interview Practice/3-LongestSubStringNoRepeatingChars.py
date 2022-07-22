class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)

        if len_s < 2: return len_s
        
        max_len = 0
        for i, c in enumerate(s):
            curr = c
            for j in range(i+1, len_s):
                if s[j] not in curr:
                    curr += s[j]
                else:
                    break
            max_len = max(len(curr), max_len)
            if max_len > (len_s-i):
                break
        return max_len


s = Solution()

tests = [
    "au",
    "abcabcbb",
    "bbbbb",
    "pwwkew",
]

for test in tests:
    print(s.lengthOfLongestSubstring(test))