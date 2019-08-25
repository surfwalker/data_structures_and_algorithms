from node import Node
import pytest

def test_Node_class_exists():
    assert Node

def test_Node_instantiation():
    assert Node('value')