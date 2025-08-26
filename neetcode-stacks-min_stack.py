# Design a stack class that supports the push, pop, top, and getMin operations.
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_seen = [float('inf')]

    def push(self, val: int) -> None:
        if val <= self.min_seen[-1]:
            self.min_seen.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_seen[-1]:
            self.min_seen.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_seen[-1]


stack = MinStack()
stack.push(-2)
stack.push(-2)
stack.push(-3)
stack.push(-3)
stack.getMin()
stack.pop()
stack.getMin()