class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        level = [root]
        while root and level:
            currentNodes = []
            next = []
            for node in level:
                currentNodes.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            answer.append(currentNodes)
            level = next
        return answer