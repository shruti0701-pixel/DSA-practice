# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None : return head  # base case
        
        len = 1
        tail = newH = head
        while tail.next:
            tail = tail.next
            len += 1
        tail.next = head
        k = k % len
        for i in range (0 , len - k):
            tail = tail.next
        newH = tail.next
        tail.next = None
        return newH