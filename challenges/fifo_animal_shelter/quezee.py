class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class Quezee():

    def __init__(self):
      self.front = None

    def peek(self):
      if self.front:
        return self.front.value
      else:
        return None

    def enqueue(self, value):
      node = Node(value)
      if self.front == None:
          self.rear = node
          self.front = node
      else:
          self.rear.next = node
          self.rear = node
    
    def dequeue(self):
      if self.front:
        node = self.front
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = node.next
        node.next = None
        return node.value
      else:
        return None