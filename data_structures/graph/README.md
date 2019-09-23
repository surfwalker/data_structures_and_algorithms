# Graphs
A graph is a collection of nodes referred to as vertices that may or may not be connected by edges to other vertices.

## API
- add_vertex(): Takes in a value. Creates a Vertex with that value and adds it to the graph's collection of vertices. Returns the newly created vertex.
- add_edge(): Takes in two vertices and an optional weight for the edge. The edge is a one-direction relationship from the first vertex passed in to the second vertex.
- get_vertices(): Returns a list of all vertices contained within the graph.
- get_neighbors(): Takes in a vertex. Returns a list of tuples for each neighbor of the vertex.
- __len__(): Returns the length of the list containing all of the vertices within the graph.