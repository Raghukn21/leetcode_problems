class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                # The second-popped operand is the LEFT side of the operation
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # token == '/'
                    # Python's // truncates toward negative infinity, not zero,
                    # so we use int(a / b) to truncate toward zero as required
                    result = int(a / b)

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]