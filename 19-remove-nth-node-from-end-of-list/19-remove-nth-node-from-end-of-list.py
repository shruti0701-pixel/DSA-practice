# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        #size of the ll - number of nodes present in ll
        count = 0
        cur = head
        while (cur != None):
            cur = cur.next
            count += 1
            
        if n == count:
            return head.next
        
        index = count - n
        prev = head
        i = 1
        while (i < index):
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return head