class Solution:
    # Solution 1) Covert to array, utilize array to BST method
    def sortedListToBST(self, head):
        # Covert linked list to array for indexing
        value_lst = []
        while head:
            value_lst.append(head.val)
            head = head.next

        # Utilize old functionality to turn array to BST
        def sortedArrayToBST(nums):
            if not nums:
                return None

            mid = len(nums)//2

            root = TreeNode(nums[mid])

            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])

            return root

        return sortedArrayToBST(value_lst)

    # Solution 2) Utilize recursion
    def sortedListToBST(self, head):
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root
