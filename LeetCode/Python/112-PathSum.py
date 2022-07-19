""" Recursive Solution """
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

""" Iterative DFS Solution """
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        stack = []
        stack.insert(0, [root, targetSum])
        while stack:
            node, curr_sum = stack.pop()
            curr_sum -= node.val
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                stack.insert(0, [node.left, curr_sum])
            if node.right:
                stack.insert(0, [node.right, curr_sum])
        return False