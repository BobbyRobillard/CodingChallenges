class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        balls = [i for i in range(len(grid[0]))]
        for i in range(len(balls)):
            while True:
                if grid[0][i] == 1: # If ball should fall right
                    if (i+1) < len(grid[0]) and grid[0][i+1] == 1: # If not on right edge and not blocked on the right
                        balls[i] += 1
                        if balls[i] + 1 == len(grid):
                            break
                    else:
                        break
                else: # If ball should fall left
                    if (i-1) >= 0 and grid[0][i-1] == -1: # If not on left edge and not blocked on the left
                        balls[i] -= 1
                        if balls[i] + 1 == len(grid):
                            break
                    else:
                        break
        return balls


s = Solution()
res = s.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])