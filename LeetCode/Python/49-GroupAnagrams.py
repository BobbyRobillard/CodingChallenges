from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped = defaultdict(list) 
        # For each string, sort it, see if it's in results
        for s in strs:
            t = "".join(sorted(list(s)))
            grouped[t].append(s)
        return list(grouped.values())

s = Solution()
res = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(res)