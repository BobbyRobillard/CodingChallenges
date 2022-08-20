class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        cnt = sum_to_i = 0
        i = 1
        while True:
            if i + sum_to_i > len(grades):
                return cnt
            cnt += 1
            sum_to_i += i
            i += 1

s = Solution()
res = s.maximumGroups([10,6,12,7,3,5])
print(res)
res = s.maximumGroups([8,8])
print(res)