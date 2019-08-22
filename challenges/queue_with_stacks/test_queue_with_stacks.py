from queue_with_stacks import PseudoQueue
import pytest

def test_pseudoqueue_exists():
    assert PseudoQueue

def test_instantiate_pseudoqueue():
    assert PseudoQueue()

def test_pseudoqueue_enqueue():
    waves = PseudoQueue()
    waves.enqueue('pipeline')
    waves.enqueue('mundaka')
    waves.enqueue('log cabins')
    expected = 'pipeline'
    actual = waves.front.value
    assert expected == actual

def test_pseudoqueue_dequeue():
    waves = PseudoQueue()
    waves.enqueue('pipeline')
    waves.enqueue('mundaka')
    waves.enqueue('log cabins')
    expected = 'pipeline'
    actual = waves.dequeue()
    assert expected == actual

def test_pseudoqueue_enqueue_stack_two_empty():
    waves = PseudoQueue()
    waves.enqueue('pipeline')
    expected = 'pipeline'
    actual = waves.stack_one.peek()
    assert actual == expected

def test_pseudoqueue_enqueue_stack_one_many():
    waves = PseudoQueue()
    waves.enqueue('pipeline')
    waves.enqueue('mundaka')
    waves.enqueue('log cabins')
    expected = 'log cabins'
    actual = waves.stack_one.peek()
    assert actual == expected

def test_pseudoqueue_dequeue_both_stacks_empty():
    waves = PseudoQueue()
    expected = None
    actual = waves.dequeue()
    assert actual == expected

def test_pseudoqueue_dequeue_both_stacks_many():
    waves = PseudoQueue()
    waves.enqueue('pipeline')
    waves.enqueue('mundaka')
    waves.enqueue('log cabins')
    waves.dequeue()
    waves.enqueue('j-Bay')
    waves.enqueue('wiamea')
    waves.enqueue('peahi')
    waves.dequeue()
    assert waves.stack_one.peek() == 'peahi'