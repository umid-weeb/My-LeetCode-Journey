# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        bahti = None
        madina = head
        while   madina:
            next_ = madina.next
            madina.next = bahti
            bahti = madina
            madina = next_
        return bahti
