class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        total = {}
        for item in items1:
            if item[0] not in total:
                total[item[0]] = item[1]
            else:
                total[item[0]] += item[1]
        for item in items2:
            if item[0] not in total:
                total[item[0]] = item[1]
            else:
                total[item[0]] += item[1]
        return sorted([[key, total[key]] for key in total], key=lambda x:x[0])

s = Solution()
res = s.mergeSimilarItems([[1,1],[4,5],[3,8]],[[3,1],[1,5]])
print(res)
res = s.mergeSimilarItems([[1,1],[3,2],[2,3]],[[2,1],[3,2],[1,3]])
print(res)
res = s.mergeSimilarItems([[1,3],[2,2]],[[7,1],[2,2],[1,4]])
print(res)