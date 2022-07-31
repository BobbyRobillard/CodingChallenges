class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

    # def generateParenthesis(self, n: int) -> list[str]:
        
    #     def generate(p, left, right, parens=[]):
    #         if left:         generate(p + '(', left-1, right)
    #         if right > left: generate(p + ')', left, right-1)
    #         if not right:    parens += p,
    #         return parens
    #     return generate('', n, n)

s = Solution().generateParenthesis(5)
print(s, "len: ", len(s))