from hashtable import HashTable
from linked_list import LinkedList, Node
import re

def repeated_word(str):
    regex = r"\W+"
    words = str.split(' ')
    hashtable = HashTable()

    for word in words:
        word = re.sub(regex, '', word).upper()
        if hashtable.contains(word):
            return word
        else:
            hashtable.add(word, None)