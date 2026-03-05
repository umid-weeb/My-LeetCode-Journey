# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        head = curr = ListNode(0)
        carry=0
        while curr1 or curr2:
            total = sum([
                curr1.val if curr1 else 0,
                curr2.val if curr2 else 0,
                carry
            ])
            digit = total%10
            carry = total//10
            curr.next= ListNode(digit)
            curr = curr.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if carry:
            curr.next= ListNode(carry)
        return head.next