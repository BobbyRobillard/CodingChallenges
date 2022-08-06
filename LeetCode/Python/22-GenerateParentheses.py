class Solution:
    def generateParenthesis(self, n):
        res = []
        self.dfs(n, n, "", res)
        return res
            
    def dfs(self, leftRemain, rightRemain, path, res):
        if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
            return  # backtracking
        if leftRemain == 0 and rightRemain == 0:
            res.append(path)
            return 
        self.dfs(leftRemain-1, rightRemain, path+"(", res)
        self.dfs(leftRemain, rightRemain-1, path+")", res)
    
    def generateParenthesis2(self, n: int) -> list[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

s = Solution().generateParenthesis(4)
print(s)