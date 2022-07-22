# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root.val == p or root.val == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        if not left and not right: return None
        return left if left else right


a = TreeNode(3)
b = TreeNode(6)
c = TreeNode(8)
a.left = b
a.right = c

d = TreeNode(2)
e = TreeNode(11)
b.left = d
b.right = e

f = TreeNode(13)
c.right = f

g = TreeNode(9)
h = TreeNode(5)
e.left = g
e.right = h

s =  Solution()
res = s.lowestCommonAncestor(a, 9, 5)
print(str(res))