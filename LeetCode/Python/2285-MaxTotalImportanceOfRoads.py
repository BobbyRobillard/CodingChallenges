class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        # 1) Calculate degree of each node
        connections = {}
        for i in range(n):
            connections[i] = 0

        for road in roads:
           connections[road[0]] += 1
           connections[road[1]] += 1

        # 2) Assign value of n to each node, greedy algo --> assign lowest n to item with least degree
        connections = [[key, connections[key]] for key in connections]
        connections.sort(key=lambda x:x[1])
        nodes_to_n = {}
        for i, conn in enumerate(connections):
            nodes_to_n[conn[0]] = i+1

        # 3) Calculate each roads importance
        return sum(nodes_to_n[road[0]] + nodes_to_n[road[1]] for road in roads)


s = Solution()
res = s.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
print(res)
res = s.maximumImportance(5, [[0,3],[2,4],[1,3]])
print(res)
res = s.maximumImportance(5, [[0,1]])
print(res)