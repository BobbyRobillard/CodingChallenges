class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        if len(matrix) == 1: return matrix[0][0]
        for i in range(len(matrix)-1):
            matrix[0] = matrix[0] + matrix[1]
            del matrix[1]
        matrix[0].sort()
        return matrix[0][k-1]

s = Solution()
print(s.kthSmallest(
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
print(s.kthSmallest(
[[1,5,9],[10,11,13],[12,13,15]], 8))
print(s.kthSmallest(
[[1,5,9],[10,11,13],[12,13,15],[10,11,13]], 8))