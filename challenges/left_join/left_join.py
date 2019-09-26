from hashtable import HashTable
from linked_list import LinkedList, Node

def left_join(synonym_ht, antonym_ht):
    key_value_results = []
    for key in synonym_ht:
        output = [key, synonym_ht[key], antonym_ht.get(key)]
        key_value_results.append(output)
    return key_value_results
