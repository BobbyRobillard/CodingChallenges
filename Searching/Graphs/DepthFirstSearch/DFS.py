from collections import deque


class Solution:

    def dfs(self, adjacency_list, s):
        """
        DFS using a stack instead of
        recursion
        Complexity: O(v + e)
        """
        parents = dict()
        stack = deque()
        stack.append((None, s))
        while len(stack) > 0:
            parent, u = stack.pop()
            if u in parents:
                continue
            parents[u] = parent
            for v in adjacency_list[u]:
                stack.append((u, v))
        return parents

    



graph = {0: [1,2],
         1: [0,2],
         2: [0,1,4],
         3: [],
         4: [2]}


s = Solution()
print(s.dfs(graph, 0))
    