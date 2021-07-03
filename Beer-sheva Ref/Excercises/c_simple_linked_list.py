from b_ll_node import Node

head = Node(0)
node = head  # Is this important?

for idx in range(1, 11):
    node.next = Node(idx)
    node = node.next

node = head

while node is not None:
    print(id(node), "->", node)
    node = node.next
