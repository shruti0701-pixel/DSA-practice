# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: return None
        
        p , q = headA , headB
        while p and q and p != q:
            p = p.next
            q = q.next
            if p == q:
                return q
            if not p:
                p = headB
            if not q:
                q = headA
        return p