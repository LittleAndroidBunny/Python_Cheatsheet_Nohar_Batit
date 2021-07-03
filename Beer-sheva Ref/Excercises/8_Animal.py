from enum import IntEnum, auto
from Hashtable_6 import Hashtable


class AninmalSpecies(IntEnum):
    cat = auto()
    dog = auto()
    horse = auto()
    cow = auto()


class Animal:
    def __init__(self, _species, _id, _name):
        self.species = _species
        self.id = _id
        self.name = _name

    def __hash__(self):  # so we can use hash() on a Animal
        return hash(self.id)  # assume id is a unique identifier

    def __eq__(self, other):  # so we can search for animals in the table
        return self.id == other.id and \
               self.species == other.species  and \
               self.name == other.name


if __name__ == '__main__':
    hash_t = Hashtable(6)

    # dogs
    for i in range(3):
        hash_t.insert(Animal(AninmalSpecies.dog, i, 'woofer'))

    # cats
    for i in range(3, 6):
        hash_t.insert(Animal(AninmalSpecies.cat, i, 'Garfield'))

    # horses
    for i in range(6, 9):
        hash_t.insert(Animal(AninmalSpecies.horse, i, 'Bucephalus'))
        # Do you know who was Bucephalus?

    print(hash_t.find(Animal(AninmalSpecies.horse, 8, 'Seabiscuit')))
    print(hash_t.find(Animal(AninmalSpecies.horse, 8, 'Bucephalus')))
