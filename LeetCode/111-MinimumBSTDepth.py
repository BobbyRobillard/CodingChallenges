class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Level order traverse the tree, checking from right to left
        answer = 0
        level = [root]
        found = False
        while root and level:
            if found:
                break
            next = []
            for node in level:
                # Whichever level is first to have a leaf-node is the answer
                if not node.left and not node.right:
                    found = True
                    break
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            level = next
            answer += 1
        return answer
