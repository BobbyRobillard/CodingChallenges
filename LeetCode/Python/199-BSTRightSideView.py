# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from itertools import chain

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

    def rightSideView(self, root) -> list[int]:
        if not root:
            return []
        if not root.right:
            return [root.val]
        return [root.val] + list(chain.from_iterable(self.levelOrder(root.right)))
