#####################################################################
# Solution #1 | Using Recurrsion
# (My personal solution)
# ------------------------------
# Runtime --> 44ms
# Memory --> 14.303MB
# ------------------------------
class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s) - 1):
            if (ord(s[i]) + 32) == ord(s[i + 1]) or ord(s[i]) == (ord(s[i + 1]) + 32):
                return self.makeGood(s[:i] + s[i + 2 :])
        return s


#####################################################################
# Solution #2 | Using Recurrsion
# Adapted from https://www.youtube.com/watch?v=4ALB5m_Idkk&ab_channel=WilliamLin
# ------------------------------
# Runtime --> 80ms
# Memory --> 13.80MB
# ------------------------------
# class Solution:
#     def makeGood(self, s: str) -> str:
#         change = True
#         while change:
#             change = False
#             temp_s = s
#             for i in range(len(s) - 1):
#                 if (ord(s[i]) + 32) == ord(s[i + 1]) or ord(s[i]) == (ord(s[i + 1]) + 32):
#                     temp_s = s[:i] + s[i + 2 :]
#                     change = True
#                     break
#             s = temp_s
#         return s


#####################################################################
# Testing, Execution Time, and Memory Useage
import time
from HelperFunctions import get_memory_used

s = Solution()
tests = [
    "leEeetcode",
    "abBAcC",
    "s",
    "aAbBcCdDeEcCfFFfgGHHhH",
]
s.makeGood("leEeetcode")

get_memory_used()
