from stacks_and_queues import Node, Stack, Quezee
import pytest

def test_node_exists():
    assert Node

def test_node_instantiation():
    assert Node('pipeline')

def test_stack_exits():
    assert Stack

def test_stack_instantiation():
    assert Stack()

def test_stack_peek_empty():
    waves = Stack()
    assert not waves.top

def test_stack_peek_full():
    waves = Stack()
    waves.push('pipeline')
    waves.push('mundaka')
    waves.push('log cabins')
    assert waves.top.value == 'log cabins'

def test_stack_push_one():
    waves = Stack()
    waves.push('pipeline')
    expected = 'pipeline'
    actual = waves.top.value
    assert expected == actual

def test_stack_push_many():
    waves = Stack()
    waves.push('pipeline')
    waves.push('mundaka')
    waves.push('log cabins')
    expected = 'log cabins'
    actual = waves.top.value
    assert expected == actual

def test_stack_pop_empty():
    waves = Stack()
    expected = None
    actual = waves.pop()
    assert expected == actual

def test_stack_pop_one():
    waves = Stack()
    waves.push('pipeline')
    waves.push('mundaka')
    waves.push('log cabins')
    expected = 'log cabins'
    actual = waves.pop()
    assert expected == actual

def test_queue_exits():
    assert Quezee

def test_queue_instantiation():
    assert Quezee()

def test_queue_enqueue_one():
    waves = Quezee()
    waves.enqueue('pipeline')
    assert waves.front.value == 'pipeline'

def test_queue_enqueue_many():
    waves = Quezee()
    waves.enqueue('pipeline')
    waves.enqueue('mundaka')
    waves.enqueue('log cabins')
    assert waves.front.value == 'pipeline'

def test_queue_dequeue():
    waves = Quezee()
    waves.enqueue('pipeline')
    waves.enqueue('mundaka')
    waves.enqueue('log cabins')
    expected = 'pipeline'
    actual = waves.dequeue()
    assert expected == actual