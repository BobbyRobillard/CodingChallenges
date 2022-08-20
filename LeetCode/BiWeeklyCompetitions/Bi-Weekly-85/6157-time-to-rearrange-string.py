class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        while True:
            if "01" in s:
                s = s.replace("01", "10")
                count += 1
            else:
                break
        return count

s = Solution()
print(s.secondsToRemoveOccurrences("0110101"))
print(s.secondsToRemoveOccurrences("11100"))