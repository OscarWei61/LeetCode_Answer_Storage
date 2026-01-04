class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mini_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.mini_stack:
            self.mini_stack.append(val)
        else:
            current_min = self.mini_stack[-1]
            self.mini_stack.append(min(val, current_min))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
        if self.mini_stack:
            self.mini_stack.pop()
        return None

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return 0
    def getMin(self):
        """
        :rtype: int
        """
        if self.mini_stack:
            return self.mini_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()