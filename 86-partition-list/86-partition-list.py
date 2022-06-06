# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1 = ListNode(0)
        d2 = ListNode(0)
        a , b = d1 , d2
        while head:
            if head.val < x:
                a.next = head
                a = a.next
            else:
                b.next = head
                b = b.next
            head = head.next
        
        a.next = d2.next
        b.next = None
        return d1.next