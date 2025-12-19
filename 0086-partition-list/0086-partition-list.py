# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        L1 = ListNode(0,None)
        L2 = ListNode(0,None)
      
        left = L1
        right = L2
        
        curr =  head
        while curr:
            nextNode = curr.next # curr.next ki value pehlay hi store krlo apnay pas

            curr.next = None # this is to break the connection....agar 1->4 rahay ga tou 
            # left mein phir yeh connection saath hi jai ga...we want 1 in it only

            if curr.val < x:
                left.next = curr
                left = left.next

            elif curr.val >= x:
                right.next = curr
                right = right.next

            curr = nextNode 
        
        left.next = L2.next
        return L1.next

    