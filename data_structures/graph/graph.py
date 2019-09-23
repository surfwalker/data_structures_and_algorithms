from collections import deque
from edge import Edge
from vertex import Vertex

class Graph():

    def __init__(self):
        self.vertices = []

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, vertex_1, vertex_2, weight=0):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            vertex_1.neighbors.append(Edge(vertex_2, weight))

    def get_neighbors(self, vertex):
        return vertex.neighbors

    def get_vertices(self):
        if len(self.vertices) == 0:
            return None
        return self.vertices

    def __len__(self):
        return len(self.vertices)