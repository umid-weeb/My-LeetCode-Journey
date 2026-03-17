class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        operators={
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b)
        }
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            operator = operators[token]
            b = stack.pop()
            a = stack.pop()
            stack.append(operator(a, b))
        return stack[0]
