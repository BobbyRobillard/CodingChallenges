class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root) -> list[list[int]]:
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

    def zigzagLevelOrder(self, root) -> list[list[int]]:
        answer = self.levelOrder(root)
        return[el[::-1] if i % 2 != 0 else el for i, el in enumerate(answer)]


s = Solution()
