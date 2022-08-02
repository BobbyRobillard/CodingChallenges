class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def arrayToBST(self, arr, i, n):
        root = None
        # Base case for recursion 
        if i < n:
            root = TreeNode(arr[i]) 
    
            # insert left child 
            root.left = self.arrayToBST(arr, 2 * i + 1, n)
    
            # insert right child 
            root.right = self.arrayToBST(arr, 2 * i + 2, n)
            
        return root

    def getDirections(self, root, startValue: int, destValue: int) -> str:
        def find(n: TreeNode, val: int, path: list[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # The idea is that we find paths for both start and target nodes.
        # Once we have found them we reduce paths to a lowest common parent node.
        # We change the all items in path of start to 'U' and keep the path of target same.
        def dfs(node, target, path):
            if not node:
                return False

            if node.val == target:
                return True

            if node.left:
                if dfs(node.left, target, path):
                    path.appendleft('L')
                    return True

            if node.right:
                if dfs(node.right, target, path):
                    path.appendleft('R')
                    return True                
            
        s_path, t_path = deque(), deque()
        dfs(root, startValue, s_path)
        dfs(root, destValue, t_path)
        
        while s_path and t_path and s_path[0] == t_path[0]:
            s_path.popleft()
            t_path.popleft()
        
        return 'U' * len(s_path) + ''.join(t_path)

s = Solution()
arr = [5,1,2,3,None,6,4]
root = s.arrayToBST(arr, 0, len(arr))
res = s.getDirections(root, 3, 6)
print(res)