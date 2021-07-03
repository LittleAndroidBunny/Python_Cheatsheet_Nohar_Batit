from e_Linked_list import LinkedList

linked = LinkedList()  # Initialize empty list

linked.add_at_start(1)  # add head
linked.add_at_start('a')  # add new head, push previous
linked.insert(1, 2)  # insert at specified location
linked.add_at_end(5)  # insert at tail
print(len(linked))  # show length
print(linked)  # show list
linked[2] = 'third'  # override third element
print(linked)  # show list

print(linked.find(1))  # find in list
loc, nod = linked.find(5)
print(loc)

linked2 = LinkedList(range(10))  # create linked list from standard sequence
print(linked2)
print(linked2.to_standard_list())
