class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            # By not evaulating right until checking left, we save lots of recursive steps if it's invalid.
            # Thus making this solution way quicker
            if left == -1:
                return -1
            right = helper(root.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return helper(root) != -1
