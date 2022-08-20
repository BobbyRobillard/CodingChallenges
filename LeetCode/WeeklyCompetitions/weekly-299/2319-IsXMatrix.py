class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        grid_len = len(grid)
        for i in range(grid_len):
            for j in range(grid_len):
                # If on a diag
                if i == j or i == grid_len - j - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True

s = Solution()
res = s.checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])
print(res)
res = s.checkXMatrix([[5,7,0],[0,3,1],[0,5,0]])
print(res)