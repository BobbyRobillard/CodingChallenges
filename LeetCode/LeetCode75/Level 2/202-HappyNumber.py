def digitSquared(n:str):
    return int(n)**2


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while True:
            n = sum(map(digitSquared, str(n)))
            if n in seen:
                return False
            if n == 1:
                return True
            seen.append(n)


s = Solution()
res = s.isHappy(19)
print(res)
res = s.isHappy(2)
print(res)
res = s.isHappy(3)
print(res)