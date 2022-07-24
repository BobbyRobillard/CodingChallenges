"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (Ri, Cj) such that row Ri and column Cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e. an equal array).
"""
class Solution:
    def equalPairs(self, rows: list[list[int]]) -> int:
        cols = []
        row_len = len(rows)
        for i in range(row_len):
            cols.append([rows[j][i] for j in range(row_len)])

        count = 0
        for col in cols:
            count += rows.count(col)
        return count
        
s = Solution()
res = s.equalPairs([[3,2,1],[1,7,6],[2,7,7]])
print(res)
res = s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
print(res)
res = s.equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]])
print(res)
res = s.equalPairs([[2,2],[2,2]])
print(res)
    