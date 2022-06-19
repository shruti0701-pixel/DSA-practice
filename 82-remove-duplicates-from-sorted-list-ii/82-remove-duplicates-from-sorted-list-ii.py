# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode (next = head)
        cur = head
        
        while cur and cur.next:
            if cur.val != cur.next.val:
                prev , cur = cur , cur.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next
        return dummy.next