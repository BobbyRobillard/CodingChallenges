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

    def findClosestNode(self, node1Paths, node2Paths):
        max_node_index = min(max(node1Paths.keys()), max(node2Paths.keys()))
        min_distance = 1_000_000_000
        min_node_index = -1
        for i in range(max_node_index + 1):
            if i in node1Paths and i in node2Paths:
                temp = max(node1Paths[i], node2Paths[i])
                if temp < min_distance:
                    min_node_index = i
                    min_distance = temp
        return min_node_index

    def closestMeetingNode(self, edges, node1, node2):
        if node1 == node2:
            return node1
        graph = self.edgesToGraph(edges)
        res = self.BFS(node1, graph)
        res2 = self.BFS(node2, graph)
        return self.findClosestNode(res, res2)


s = Solution()
print(s.closestMeetingNode([1, 2, -1], 0, 2))
