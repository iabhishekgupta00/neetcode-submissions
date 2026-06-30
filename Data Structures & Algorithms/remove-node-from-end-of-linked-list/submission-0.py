# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        s , f = dummy , dummy

        for _ in range(n+1):
            f = f.next
        
        while f:
            s = s.next
            f = f.next

        s.next = s.next.next

        return dummy.next


        