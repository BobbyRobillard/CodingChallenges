""" 
LeetCode - 1971
----------------
Given edges and the integers n, source, and destination, 
return true if there is a valid path from source to destination, or false otherwise.
"""

from collections import defaultdict


def validPath(n, edges, src, dst):

    # Create the graph
    neighbors = defaultdict(list)
    for n1, n2 in edges:
        neighbors[n1].append(n2)
        neighbors[n2].append(n1)

    # Use Depth First Search to determine if there is a path to the node.
    # Use visited to avoid infinite cycles.
    visited = set()
    def dfs(node):
        if node == dst: return True
        if node not in visited:
            visited.add(node)
            for edge in neighbors[node]:
                result = dfs(edge)
                if result: return True
    
    return dfs(src)


# --------------------------------------
#               DRIVER CODE
# --------------------------------------


tests = [
    {
        "n": 10,
        "edges": [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]],
        "source": 5,
        "destination": 9
    },
]

for test in tests:
    print(
        validPath(
            test['n'], test['edges'], test['source'], test['destination']
        )
    )