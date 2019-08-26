from quezee import Node, Quezee

class Animal:
    def __init__(self, species, name):
        self.name = name
        self.species = species
        
class AnimalShelter:
    def __init__(self):
        self.animal_queue = Quezee()

    def enqueue(self, animal):
        self.animal_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref not in ('dog', 'cat'):
            return None
        if self.animal_queue.front:
            current = self.animal_queue.front
            previous = None
            while current.value.species != pref:
                previous = current
                current = current.next
            if previous:
                previous.next = current.next
            else:
                self.animal_queue.front = current.next
            current.next = None
            return current.value
        return None
