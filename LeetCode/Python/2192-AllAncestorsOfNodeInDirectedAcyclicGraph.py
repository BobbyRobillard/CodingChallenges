from collections import defaultdict


""" EASY TO UNDERSTAND BUT SLOW SOLUTION """
class Solution:
    def dfs(self, graph, source):
       if source is None or source not in graph:
           return "Invalid input"

       path = []
       stack = [source]
       while(len(stack) != 0):
           s = stack.pop()
           if s not in path:
               path.append(s)
           if s not in graph:
               continue
           for neighbor in graph[s]:
               stack.append(neighbor)
       return path

    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # Create graph from edge list
        graph = {}
        for edge in edges:
            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        # DFS for each node, all nodes reachable from curr have curr as an ancestor
        result = {}
        for node in graph:
            result[node] = self.dfs(graph, node)
            result[node].remove(node)
        # Return answer in correct format
        return [sorted(result[i]) if i in result else [] for i in range(n)]


""" MUCH FASTER (and accepted) SOLUTION """
class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        
        def dfs(ancestor: int, kid: int) -> None:
            if not (ans[kid] and ans[kid][-1] == ancestor):
                if kid != ancestor:
                    ans[kid].append(ancestor)
                for grand_child in parent_to_kids[kid]:
                    dfs(ancestor, grand_child)

        parent_to_kids = defaultdict(list)
        for parent, kid in edges:
            parent_to_kids[parent].append(kid)
        ans = [[] for _ in range(n)]
        for i in range(n):
            dfs(i, i)
        return ans


s = Solution()
res = s.getAncestors(48, [[23,5],[23,31],[23,44],[23,20],[23,28],[23,38],[23,47],[23,16],[23,17],[23,36],[23,18],[23,25],[23,33],[23,32],[23,0],[23,43],[23,37],[23,41],[23,9],[23,24],[23,10],[23,39],[23,1],[46,31],[46,47],[46,16],[46,29],[46,18],[46,25],[46,4],[46,30],[46,27],[46,35],[46,0],[46,9],[46,24],[46,39],[46,1],[42,31],[42,6],[42,20],[42,38],[42,16],[42,17],[42,2],[42,36],[42,12],[42,29],[42,25],[42,33],[42,4],[42,30],[42,27],[42,32],[42,45],[42,7],[42,10],[5,14],[5,44],[5,28],[5,40],[5,38],[5,47],[5,8],[5,2],[5,36],[5,12],[5,33],[5,43],[5,10],[5,39],[5,21],[14,6],[14,44],[14,28],[14,13],[14,38],[14,47],[14,34],[14,8],[14,17],[14,36],[14,18],[14,25],[14,33],[14,4],[14,30],[14,27],[14,35],[14,0],[14,19],[14,37],[14,41],[14,24],[14,45],[14,10],[14,1],[31,28],[31,40],[31,26],[31,22],[31,16],[31,17],[31,29],[31,25],[31,4],[31,32],[31,43],[31,37],[31,9],[31,24],[31,7],[31,39],[31,1],[31,21],[6,44],[6,3],[6,15],[6,40],[6,13],[6,47],[6,34],[6,16],[6,2],[6,29],[6,18],[6,4],[6,11],[6,35],[6,0],[6,43],[6,37],[6,7],[6,10],[6,1],[6,21],[44,20],[44,28],[44,40],[44,47],[44,16],[44,17],[44,33],[44,30],[44,11],[44,19],[44,9],[44,1],[3,15],[3,20],[3,26],[3,22],[3,2],[3,36],[3,11],[3,27],[3,35],[3,32],[3,0],[3,37],[3,41],[3,24],[3,39],[15,26],[15,47],[15,4],[15,30],[15,11],[15,43],[15,19],[15,45],[15,10],[20,47],[20,34],[20,16],[20,2],[20,12],[20,33],[20,4],[20,30],[20,11],[20,35],[20,43],[20,19],[20,41],[20,9],[20,21],[28,40],[28,16],[28,36],[28,25],[28,35],[28,32],[28,19],[28,41],[28,24],[28,21],[40,13],[40,38],[40,47],[40,34],[40,16],[40,2],[40,36],[40,12],[40,29],[40,18],[40,4],[40,27],[40,0],[40,41],[40,9],[40,10],[40,1],[26,13],[26,38],[26,22],[26,34],[26,16],[26,25],[26,33],[26,27],[26,35],[26,32],[26,19],[26,39],[26,1],[26,21],[13,38],[13,34],[13,17],[13,2],[13,12],[13,25],[13,33],[13,30],[13,35],[13,0],[13,43],[13,19],[13,37],[13,9],[13,39],[13,1],[38,22],[38,47],[38,8],[38,17],[38,2],[38,12],[38,18],[38,25],[38,4],[38,30],[38,35],[38,32],[38,9],[38,7],[38,10],[22,34],[22,16],[22,36],[22,12],[22,29],[22,25],[22,4],[22,30],[22,11],[22,35],[22,0],[22,43],[22,41],[22,24],[22,45],[22,1],[47,8],[47,16],[47,17],[47,36],[47,33],[47,11],[47,27],[47,19],[47,37],[47,41],[47,24],[34,12],[34,29],[34,30],[34,32],[34,37],[34,45],[34,39],[8,17],[8,2],[8,36],[8,18],[8,33],[8,4],[8,35],[8,37],[8,45],[8,7],[16,17],[16,12],[16,18],[16,25],[16,4],[16,32],[16,0],[16,19],[16,39],[16,1],[17,18],[17,30],[17,11],[17,35],[17,0],[17,7],[2,36],[2,12],[2,29],[2,33],[2,4],[2,30],[2,11],[2,35],[2,43],[2,19],[2,41],[2,24],[2,45],[2,10],[2,1],[36,29],[36,25],[36,33],[36,11],[36,27],[36,19],[36,37],[36,41],[36,24],[36,10],[36,21],[12,33],[12,4],[12,0],[12,43],[12,9],[12,24],[12,7],[29,18],[29,30],[29,11],[29,32],[29,0],[29,37],[29,41],[29,24],[29,10],[29,39],[29,1],[29,21],[18,25],[18,4],[18,30],[18,35],[18,19],[18,41],[18,24],[18,7],[18,1],[25,4],[25,11],[25,35],[25,0],[25,37],[25,41],[25,24],[25,45],[25,39],[25,21],[33,4],[33,30],[33,11],[33,27],[33,43],[33,19],[33,37],[4,35],[4,37],[4,41],[4,9],[4,24],[4,39],[4,1],[4,21],[30,11],[30,27],[30,43],[30,19],[30,41],[30,9],[30,24],[30,7],[11,35],[11,32],[11,43],[11,37],[11,45],[27,35],[27,0],[27,43],[27,37],[27,45],[27,10],[27,1],[27,21],[35,21],[32,0],[32,43],[32,19],[32,37],[32,41],[32,9],[32,10],[0,37],[0,45],[0,7],[43,37],[43,24],[43,45],[43,10],[43,1],[19,37],[19,41],[19,9],[19,24],[19,39],[19,21],[37,41],[37,10],[41,9],[41,45],[41,39],[41,21],[9,24],[9,45],[9,7],[9,39],[24,45],[24,7],[24,10],[45,21],[7,21],[10,21],[1,21]])
print(res)