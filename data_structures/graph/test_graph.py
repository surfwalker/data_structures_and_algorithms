from graph import Graph
from edge import Edge
from vertex import Vertex
import pytest

def test_class_Graph_exists():
    assert Graph

def test_class_Vertex_exists():
    assert Vertex

def test_Vertex_instantiation():
    assert Vertex('value')

def test_no_nodes_in_graph():
    graph = Graph()
    expected = None
    actual = graph.get_vertices()
    assert actual == expected

def test_add_vertex_single_to_graph():
    graph = Graph()
    waves = graph.add_vertex('waves')
    expected = 'waves'
    actual = waves.value
    assert actual == expected

def test_add_vertex_multiple_to_graph():
    graph = Graph()
    waves = graph.add_vertex('waves')
    surfers = graph.add_vertex('surfers')
    sponsors = graph.add_vertex('sponsors')
    assert waves.value == 'waves'
    assert surfers.value == 'surfers'
    assert sponsors.value == 'sponsors'

def test_get_vertex_single_from_graph():
    graph = Graph()
    graph.add_vertex('waves')
    vertex_results = graph.get_vertices()
    assert [vertex.value for vertex in vertex_results] == ['waves']

def test_get_vertex_multiple_from_graph():
    graph = Graph()
    graph.add_vertex('waves')
    graph.add_vertex('surfers')
    graph.add_vertex('sponsors')
    vertex_results = graph.get_vertices()
    assert {vertex.value for vertex in vertex_results} == set(['waves', 'surfers', 'sponsors'])

def test_return_total_nodes_in_graph():
    graph = Graph()
    graph.add_vertex('waves')
    graph.add_vertex('surfers')
    graph.add_vertex('sponsors')
    expected = 3
    actual = len(graph)
    assert actual == expected

def test_get_single_node_and_single_edge_properly_returned():
    graph = Graph()
    waves = graph.add_vertex('waves')
    graph.add_edge(waves, waves, 69)

def test_get_node_neighbors_in_graph():
    graph = Graph()
    waves = graph.add_vertex('waves')
    surfers = graph.add_vertex('surfers')
    sponsors = graph.add_vertex('sponsors')
    graph.add_edge(waves, surfers, 10)
    graph.add_edge(waves, sponsors, 20)
    graph.add_edge(surfers, sponsors, 30)
    node_neighbors = graph.get_neighbors(waves)
    assert node_neighbors[0].vertex.value == 'surfers'
    assert node_neighbors[0].weight == 10
    assert node_neighbors[1].vertex.value == 'sponsors'
    assert node_neighbors[1].weight == 20