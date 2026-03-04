class Solution:
    def find_midle(slef, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_= curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev
    def isSame(self, h1, h2):
        while h2:
            if h1.val!=h2.val:
                return False
            h1= h1.next
            h2= h2.next
        return True
    def isPalindrome(self, head):
        middle = self.find_midle( head)
        second = self.reverse(middle)
        return self.isSame(head, second)
        
