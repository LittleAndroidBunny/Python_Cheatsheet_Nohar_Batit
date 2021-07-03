from b_ll_node import Node


class LinkedList:  # Why doesn't the class inherit the node class?

    def __init__(self, seq=None):
        """
        Linked list init function

        :param seq: Use seq != none to generate a linked list from any python sequence type
        """

        self.next = None
        self.length = 0
        if seq is not None:
            for x in seq[::-1]:
                self.add_at_start(x)  # Use add_at_start in reverse order due to O(1) complexity for each insertion

    def __repr__(self):
        out = ""
        p = self.next
        while p is not None:
            out += str(p) + " -> "  # str invokes __repr__ of class Node
            p = p.next
        return out

    def __len__(self):
        """ called when using Python's length() """
        return self.length

    def add_at_start(self, val):
        """ add node with value val at the list head """
        p = self
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.length += 1

    def add_at_end(self, val):
        """ add node with value val at the list tail """
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)
        self.length += 1

    def insert(self, loc, val):
        """ add node with value val after location 0<=loc<length of the list """
        assert 0 <= loc < len(self)
        p = self
        for i in range(0, loc):
            p = p.next
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.length += 1

    def __getitem__(self, loc):
        """ called when using L[i] for reading
            return node at location 0<=loc<length """
        assert 0 <= loc < len(self)
        p = self.next
        for i in range(0, loc):
            p = p.next
        return p

    def __setitem__(self, loc, val):
        """ called when using L[loc]=val for writing
            assigns val to node at location 0<=loc<length """
        assert 0 <= loc < len(self)
        p = self.next
        for i in range(0, loc):
            p = p.next
        p.value = val
        return None

    def find(self, val):
        """ find (first) node with value val in list """
        p = self.next
        loc = 0  # in case we want to return the location
        while p is not None:
            if p.value == val:
                return loc, p
            else:
                p = p.next
                loc = loc + 1  # in case we want to return the location
        return None

    def delete(self, loc):
        """ delete element at location 0<=loc<length """
        assert 0 <= loc < len(self)
        p = self
        for i in range(0, loc):
            p = p.next
        # p is the element BEFORE loc
        p.next = p.next.next
        self.length -= 1

    def insert_ordered(self, val):
        """ assume self is an ordered list,
            insert Node with val in order """
        p = self
        q = self.next
        while q is not None and q.value < val:
            p = q
            q = q.next
        new_node = Node(val)
        p.next = new_node
        new_node.next = q
        self.length += 1

    def find_ordered(self, val):
        """ assume self is an ordered list,
            find Node with value val """
        p = self.next
        while p is not None and p.value < val:
            p = p.next
        if p is not None and p.value == val:
            return p
        else:
            return None

    def reverse(self):
        prev = None
        curr = self.next
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.next = prev
        return self

    def to_standard_list(self):
        result = [None] * len(self)
        p = self.next
        for i in range(len(self)):
            result[i] = p.value
            p = p.next
        return result
