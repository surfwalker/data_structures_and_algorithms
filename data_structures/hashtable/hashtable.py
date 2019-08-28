from linked_list import LinkedList

class HashTable:
    
    def __init__(self):
        self.buckets = [LinkedList()] * 1024

    def hash(self, key):
        char_sum = sum([ord(char) for char in key])
        index = char_sum * 599 % len(self.buckets)
        return index

    def add(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        bucket.insert({'key':key, 'value':value})

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        value = None
        if bucket.head:
            current = bucket.head
            while current:
                if current.value['key'] == key:
                    value = current.value['value']
                    break
                current = current.next
        return value

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket.head:
            current = bucket.head
            while current:
                if current.value['key'] == key:
                    return True
                current = current.next
        return False