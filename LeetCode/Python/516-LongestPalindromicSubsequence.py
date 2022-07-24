class Solution:
    def longestPalindromeSubseq(self, s):
        """
        Use DP
        """
        str_len = len(s)
        dp_matrix = [[0]*len(s) for i in range(str_len)]
        
        k = 0
        while k < str_len:
            for i in range(str_len-k):
                j = i + k
                if i == j:
                    dp_matrix[i][j] = 1
                elif s[i] == s[j]:
                    dp_matrix[i][j] = dp_matrix[i+1][j-1] + 2
                else:
                    dp_matrix[i][j] = max(dp_matrix[i][j-1], dp_matrix[i+1][j])
            k += 1
                 
        return dp_matrix[0][str_len-1]

s = Solution()
tests = [
    "bbbab",
    "cbbd"
]
for test in tests:
    print(s.longestPalindromeSubseq(test))