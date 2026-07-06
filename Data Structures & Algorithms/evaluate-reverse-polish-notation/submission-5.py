class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = None
        b = None
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            elif len(stack)>1:
                if token == "+":
                    result = stack[-2] + stack[-1]
                elif token == "-":
                    result = stack[-2] - stack[-1]
                elif token == "*":
                    result = stack[-2] * stack[-1]
                elif token == "/":
                    result = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
    
        return stack[-1]