# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse after slow
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        #comapring first node and reversed first node - values
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
                
            
        