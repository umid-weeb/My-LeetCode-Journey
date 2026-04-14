class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack=[]
        for c in s:
            stack.append(c)
        i=0
        while stack:
            s[i] = stack.pop()
            i+=1