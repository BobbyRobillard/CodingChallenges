# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head) -> list[list[int]]:
        #1) Create M by N Matrix
        res = [[-1 for j in range(n)] for i in range(m)] 
        #2) Initialize starting values to fill from
        x = y = 0
        dx, dy = 1, 0
        #3) While we have values left in the list
        while head:
            #4) Add the newest value to the result
            res[y][x] = head.val
            #5) Calculate new x, y position to insert at
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m or \
                res[y+dy][x+dx] != -1:
                dx, dy = -dy, dx
            x = x + dx
            y = y + dy
            #6) Update head
            head = head.next
        return res
