class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s) - 1):
            if (ord(s[i]) + 32) == ord(s[i+1]) or ord(s[i]) == (ord(s[i+1]) + 32):
                return self.makeGood(s[:i] + s[i+2:])
        return s

tests = ["leEeetcode","abBAcC","s"]
s = Solution()
for t in tests:
    print("IN: {0} -> OUT: {1}".format(t, s.makeGood(t)))
