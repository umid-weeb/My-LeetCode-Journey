from collections import Counter
class Solution:
    def isValid(self, s: str) -> bool:
        open_=['(', '[', '{']
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack=[]
        for i in s:
            if i in open_:
                stack.append(i)
            elif stack and i== pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack)==0