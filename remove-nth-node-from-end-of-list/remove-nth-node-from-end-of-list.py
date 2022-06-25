# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None: return None
        
        #size of the ll
        count = 0
        cur = head
        while (cur != None):
            cur = cur.next
            count += 1
        
        if (n == count):
            return head.next
        
        indextofind = count - n
        prev = head
        cp = 1    #current position
        
        while (cp < indextofind):
            prev = prev.next
            cp += 1
        prev.next = prev.next.next
        return head
            
            
            
            
            
            
            
            
            
            