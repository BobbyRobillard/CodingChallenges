class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        seen = []
        # Make list of all values seen so far
        for intr in intervals:
            for val in list(range(intr[0], intr[1]+1)):
                if val not in seen:
                    seen.append(val)
        # Loop through all values, marking where there are gaps
        intervals = []
        curr = [seen[0]]
        for i in range(1, len(seen) - 1):
            if seen[i] + 1 != seen[i+1]:
                curr.append(seen[i])
                intervals.append(curr)
                curr = []
            else:
                curr.append(seen[i])
        if seen[-1] == seen[-2] + 1:
            curr.append(seen[-1])
            intervals.append(curr)
        else:
            intervals.append(curr)
            intervals.append([seen[-1]])
        return [[intr[0], intr[-1]] for intr in intervals]


s = Solution()
res = s.merge([[1,3],[2,6],[8,10],[15,18]])
print(res)