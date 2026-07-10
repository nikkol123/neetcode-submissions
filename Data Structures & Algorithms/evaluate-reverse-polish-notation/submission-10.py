import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        for token in tokens:
            if token in "+-*":
                sign = token
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.append(ops[sign](arg1, arg2))
            elif token == "/":
                sign = token
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.append(int(arg1/arg2))
            
            else:
                stack.append(int(token))
        return stack.pop()