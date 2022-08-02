class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        if len(matrix) == 1: return matrix[0][0]
        if len(matrix) % 2 == 0:
            for i in range(len(matrix)//2):
                matrix[0] = matrix[0] + matrix[1]
                del matrix[1]
        else:
            for i in range(len(matrix)//2 + 1):
                matrix[0] = matrix[0] + matrix[1]
                del matrix[1]
        matrix[0].sort()
        return matrix[0][k-1]

s = Solution()
print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))