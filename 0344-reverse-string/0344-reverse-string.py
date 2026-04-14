class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(l, r):
            if l<r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        reverse(0, len(s)-1)
