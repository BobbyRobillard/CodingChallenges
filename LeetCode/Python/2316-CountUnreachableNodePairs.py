from collections import defaultdict


class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        #1) Create graph from edges
        graph = self.makeGraph(edges)

        #2) DFS each unvisited node to find all the connected components
        visited = []
        components = defaultdict(list)
        for i in range(n):
            if i not in visited:
                components[i] = self.dfs(i, graph)
                visited.append(i)
                for j in components[i]:
                    if j not in visited:
                        visited.append(j)

        #3) Calculate total unreachable pairs
        total = 0
        while len(components) > 1:
            total += len(components[0]) * sum(len(comp) for comp in components[1:])
            components = components[1:]
        return total
        

    def dfs(self):
        pass

    def makeGraph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph


s = Solution()
s.countPairs(3, [[0,1],[0,2],[1,2]])