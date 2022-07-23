from collections import Counter

class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if 5 * [suits[0]] == suits:
            return "Flush"
        max_count = 0
        counts = Counter(ranks)
        for key in counts.keys():
            max_count = max(max_count, counts[key])
        if max_count >= 3:
            return "Three of a Kind"
        if max_count == 2:
            return "Pair"
        return "High Card"
s = Solution()
res = s.bestHand([13,2,3,1,9], ["a","a","a","a","a"])
print(res)
res = s.bestHand([4,4,2,4,4], ["d","a","a","b","c"])
print(res)