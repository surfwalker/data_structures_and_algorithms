class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False