class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operation_list = ['+', '-', '*', '/']
        stack = []
        
        for c in tokens:
            if c not in operation_list:
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if c == '+':
                    stack.append(num1 + num2)
                elif c == '-':
                    stack.append(num1 - num2)
                elif c == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(float(num1) / num2))
        
        return stack[0]