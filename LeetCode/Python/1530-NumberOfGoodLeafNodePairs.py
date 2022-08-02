class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findLeafNodes(self, root):
        return []
    
    def findDistance(self, node1, node2):
        return 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Find all leaf nodes
        leaves = self.findLeafNodes()
        # For each leaf node not visited, calculate distance to all others, if distance <= target then count += 1
        visited = []
        count = 0
        for leaf1 in leaves:
            for leaf2 in leaves:
                if leaf1 != leaf2:
                    t = sorted([leaf1, leaf2], key=lambda x:x.val)
                    if t not in visited:
                        visited.append(t)
                        if self.findDistance(leaf1, leaf2) <= distance:
                            count += 1
        return count
