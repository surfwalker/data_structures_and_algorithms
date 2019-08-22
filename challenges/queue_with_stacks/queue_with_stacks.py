from stack import Stack

class PseudoQueue:

    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()

    def enqueue(self, value):
        self.stack_one.push(value)
        if self.stack_one.top.next == None:
            self.front = self.stack_one.top

    def dequeue(self):
        while self.stack_one.top:
            node = self.stack_one.pop()
            self.stack_two.push(node)
        queue_front = self.stack_two.pop()
        self.front = self.stack_two.top
        while self.stack_two.top:
            node = self.stack_two.pop()
            self.stack_one.push(node)
        return queue_front