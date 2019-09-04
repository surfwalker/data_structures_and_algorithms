from fifo_animal_shelter import Animal, AnimalShelter
from quezee import Node, Quezee
import pytest

def test_Node_class_exits():
    assert Node

def test_Node_instantiation():
    assert Node('value') 

def test_AnimalShelter_class_exits():
    assert AnimalShelter

def test_AnimalShelter_instantiation():
    assert AnimalShelter()

def test_quezee_class_exits():
    assert Quezee

def test_quezee_instantiation():
    assert Quezee()

def test_Animal_class_exits():
    assert Animal

def test_Animal_instantiation():
    assert Animal('dog', 'glen')

def test_enqueue_one_dog():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Animal('dog', 'glen'))
    assert animal_shelter.dequeue('dog').name == 'glen'

def test_enqueue_many_dogs():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Animal('dog', 'glen'))
    animal_shelter.enqueue(Animal('dog', 'tweedie'))
    animal_shelter.enqueue(Animal('dog', 'dusty'))
    assert animal_shelter.dequeue('dog').name == 'glen'
    assert animal_shelter.dequeue('dog').name == 'tweedie'
    assert animal_shelter.dequeue('dog').name == 'dusty'

def test_enqueue_one_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Animal('cat', 'whiskers'))
    assert animal_shelter.dequeue('cat').name == 'whiskers'

def test_enqueue_many_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Animal('cat', 'whiskers'))
    animal_shelter.enqueue(Animal('cat', 'autumn'))
    animal_shelter.enqueue(Animal('cat', 'chloe'))
    assert animal_shelter.dequeue('cat').name == 'whiskers'
    assert animal_shelter.dequeue('cat').name == 'autumn'
    assert animal_shelter.dequeue('cat').name == 'chloe'

def test_dequeue_dogs_and_cats():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Animal('dog', 'glen'))
    animal_shelter.enqueue(Animal('cat', 'whiskers'))
    animal_shelter.enqueue(Animal('dog', 'tweedie'))
    animal_shelter.enqueue(Animal('cat', 'autumn'))
    animal_shelter.enqueue(Animal('dog', 'dusty'))
    animal_shelter.enqueue(Animal('cat', 'chloe'))
    assert animal_shelter.dequeue('dog').name == 'glen'
    assert animal_shelter.dequeue('cat').name == 'whiskers'
    assert animal_shelter.dequeue('dog').name == 'tweedie'
    assert animal_shelter.dequeue('cat').name == 'autumn'
    assert animal_shelter.dequeue('dog').name == 'dusty'
    assert animal_shelter.dequeue('cat').name == 'chloe'

def test_dequeue_preference_not_dog_or_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Animal('dog', 'glen'))
    animal_shelter.enqueue(Animal('cat', 'whiskers'))
    assert animal_shelter.dequeue('monkey') == None