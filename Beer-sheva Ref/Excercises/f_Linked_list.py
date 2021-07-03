import time

from e_Linked_list import LinkedList
from b_ll_node import Node


def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print("{} took {:.4f} s".format(func.__name__, (t2 - t1)))
        return res

    return wrapper


@print_timing
def add_in_middle_linked_list(lst, n):
    p = lst
    for i in range(n):
        tmp = p.next
        p.next = Node(chr((i % 26) + 65))
        p.next.next = tmp
        lst.length += 1
        for j in range(10):
            if p != None:
                p = p.next


@print_timing
def add_to_head_linked_list(lst, n):
    for i in range(n):
        lst.add_at_start(chr((i % 26) + 65))


@print_timing
def add_to_tail_linked_list(lst, n):
    lst.reverse()
    for i in range(n):
        lst.add_at_start(chr((i % 26) + 65))
    lst.reverse()


@print_timing
def add_in_middle_list(lst, n):
    for i in range(n):
        lst.insert(10 * i, chr((i % 26) + 65))


@print_timing
def add_to_head_list(lst, n):
    for i in range(n):
        lst.insert(0, chr((i % 26) + 65))


@print_timing
def add_to_tail_list(lst, n):
    for i in range(n):
        lst.extend(chr((i % 26) + 65))


power = 6
num = 10 ** power
ls = list(range(num))
linked = LinkedList(ls)
# add 10^4 elements
n2 = 10 ** (power - 2)
add_in_middle_linked_list(linked, n2)
add_in_middle_list(ls, n2)
add_to_head_linked_list(linked, n2)
add_to_head_list(ls, n2)
add_to_tail_linked_list(linked, n2)
add_to_tail_list(ls, n2)

print(ls == linked.to_standard_list())
