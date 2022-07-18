# ----------------------------------------------
#           RECURSIVE BFS
# ----------------------------------------------

# def bfs(root):
#     if not root:
#         return []
#     left_values = dfs(root.left)
#     right_values = dfs(root.right)
#     return [root] + left_values + right_values

# ----------------------------------------------
#           ITERATIVE BFS
# ----------------------------------------------

def bfs(root):
    if not root: return []

    result = []
    queue = [root]
   
    while queue:
        curr = queue.pop(0)
        result.append(curr)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result

# ----------------------------------------------
#           DRIVER CODE & TESTING
# ----------------------------------------------
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return str(self.val)

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f

for item in bfs(a):
    print(item)