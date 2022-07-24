class Solution:
    """ Initial Brute Force Solution, too slow, times out. """
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        s_len = len(s)
        if s_len == 1: return s
        for i, el in enumerate(s):
            for j in range(s_len - 1, i, -1):
                if el == s[j]:
                    slice = s[i:j+1]
                    reverse = s[i:j+1][::-1]
                    if slice == reverse:
                        longest = slice if len(slice) > len(longest) else longest
        return longest if len(longest) > 0 else s[0]

    """ Better solution, splits ranges and specalizes based on s length """
    def longestPalindrome(self, s: str) -> str:
        def helper(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        res = ""
        for i in range(len(s)):
            # Odd Case
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # Even Case
            tmp = helper(s, i, i+1)     
            if len(tmp) > len(res):
                res = tmp
        return res

s = Solution()
tests = ["babad", "cbbd"]
for test in tests:
    print(s.longestPalindrome(test))