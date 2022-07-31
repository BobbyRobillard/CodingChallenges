import itertools

class Solution:
    def dfs(self, root):
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

    def kthSmallest(self, root, k):
        nodes = self.dfs(root)
        vals = [node.val for node in nodes]
        print(vals)
        vals.sort()
        return vals[k-1]


class Solution:
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, root, result):
        if root:
            self.helper(root.left, result)
            result.append(root.val)
            self.helper(root.right, result)

    def kthSmallest(self, root, k):
        if not root.left and not root.right:
            return root.val
        
        count_left = 0
        left_vals = []
        if root.left:
            left_vals = self.inorderTraversal(root.left) + root.val
            if len(left_vals) >= k:
                return sorted(left_vals)[k-1]
        count_left = len(left_vals)
        if root.right:
            right_vals = self.inorderTraversal(root.right)
            return sorted(right_vals)[k-len(left_vals)-1]


        # nodes = self.dfs(root)
        # vals = [node.val for node in nodes]
        # vals.sort()
