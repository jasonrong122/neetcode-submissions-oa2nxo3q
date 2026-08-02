class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2 = self.stack1[::-1]

    def pop(self) -> int:
        self.stack2.pop()
        self.stack1 = self.stack1[::-1]

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return self.stack1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()