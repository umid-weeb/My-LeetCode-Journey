# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = head
        while n>0 and right:
            right = right.next
            n-=1
            #shifting pinters
        while right:
            left = left.next
            right = right.next
        #delete part of n
        left.next = left.next.next
        return dummy.next