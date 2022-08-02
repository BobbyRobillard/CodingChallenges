def hasPath(self, root, arr, x): 
        
        # if root is None there is no path  
        if (not root): 
            return False
        
        # push the node's value in 'arr'  
        arr.append(root.val)      
        
        # if it is the required node  
        # return true  
        if (root.val == x):      
            return True
        
        # else check whether the required node  
        # lies in the left subtree or right  
        # subtree of the current node  
        if (self.hasPath(root.left, arr, x) or 
            self.hasPath(root.right, arr, x)):  
            return True
        
        # required node does not lie either in  
        # the left or right subtree of the current  
        # node. Thus, remove current node's value   
        # from 'arr'and then return false      
        arr.pop(-1)  
        return False

def findPath(self, A, B):
    ans=[]
    self.hasPath(A,ans,B)
    return ans