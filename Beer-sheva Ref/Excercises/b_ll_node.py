
class Node:
    next: None

    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return "[" + str(self.value) + "," + str(id(self.next)) + "]"
