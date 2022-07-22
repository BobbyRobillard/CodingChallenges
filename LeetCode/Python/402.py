import itertools

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        combs = [''.join(x) for x in itertools.combinations(num, k)]
        print(str(combs))
        return min(lst)
 

s = Solution()
s.removeKdigits('8168172', 3)