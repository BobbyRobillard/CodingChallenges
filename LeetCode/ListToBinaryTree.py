# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertLevelOrder(self, arr, i, n):
        root = None
        # Base case for recursion 
        if i < n:
            root = TreeNode(arr[i]) 
    
            # insert left child 
            root.left = self.insertLevelOrder(arr, 2 * i + 1, n)
    
            # insert right child 
            root.right = self.insertLevelOrder(arr, 2 * i + 2, n)
            
        return root

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

s = Solution()
arr = [5,1,2,3,None,6,4]
root = s.insertLevelOrder(arr, 0, len(arr))
print(s.levelOrder(root))