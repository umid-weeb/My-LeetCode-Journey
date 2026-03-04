class Solution:
    def isPalindrome(self, head):

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True