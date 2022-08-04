from collections import defaultdict


class Solution:
    def BFS(self, start, graph):
        i = 1
        level = {start: 0}
        parent = {start: None}
        frontier = [start]  # level = i - 1
        while frontier:
            next = []  # level = i
            for u in frontier:
                for v in graph[u]:
                    if v not in level:
                        level[v] = i
                        parent[v] = u
                        next.append(v)
            frontier = next
            i += 1
        return level

    def edgesToGraph(self, edges):
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            if edge != -1:
                graph[i].append(edge)
        return graph


s = Solution()
graph = s.edgesToGraph([2, 2, 3, -1])
res = s.BFS(0, graph)
res2 = s.BFS(1, graph)
print(res)
print(res2)
