class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        # Get list length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        i = 0
        curr = head
        while i < length - n:
            curr = curr.next
            i += 1
        curr = curr.next.next
        return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
s = Solution()
res = s.removeNthFromEnd(a, 2)
while(res):
    print(res.val)
    res = res.next