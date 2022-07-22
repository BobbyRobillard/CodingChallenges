# ----------------------------------------------
#           RECURSIVE DFS
# ----------------------------------------------

def dfs(root):
    if not root:
        return []
    left_values = dfs(root.left)
    right_values = dfs(root.right)
    return [root] + left_values + right_values

# ----------------------------------------------
#           ITERATIVE DFS
# ----------------------------------------------

def dfs(root):
    result = []
    stack = [root]
    while stack:
        curr = stack.pop()
        result.append(curr)
        if curr.left:
            stack.insert(0, curr.left)
        if curr.right:
            stack.insert(0, curr.right)
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

a = Node(5)
b = Node(1)
c = Node(2)
d = Node(6)
e = Node(8)
f = Node(3)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f

for item in dfs(a):
    print(item)