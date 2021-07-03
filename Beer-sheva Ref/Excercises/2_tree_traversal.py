class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:  # if new data is smaller insert in left
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:  # if new data is larger insert in right
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # In order traversal
    def in_order_traversal(self):

        # Set current to root of binary tree
        current = self
        stack = []  # initialize stack
        result = list()

        while True:
            # Reach the left most Node of the current Node
            if current is not None:
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)
                current = current.left

            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    result.append(current.data)

                    # We have visited the node and its left
                    # subtree. Now, it's right subtree's turn
                    current = current.right

                else:
                    break
        return result

    # pre order traversal
    def pre_order_traversal(self):
        current = self
        stack = []  # initialize stack
        result = list()

        if self is None:  # is root is none
            return result
        else:  # initialize stack
            stack.append(current)

        while len(stack) > 0:

            # Pop the top item from stack and print it
            node = stack.pop()
            result.append(node.data)

            # Push right and left children of the popped node
            # to stack
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result

    # post order traversal
    def post_order_traversal(self):
        if self is None:
            return

        result = []

        # Create two stacks
        s1 = []
        s2 = []

        # Push root to first stack
        s1.append(root)

        # Run while first stack is not empty
        while len(s1) > 0:

            # Pop an item from s1 and append it to s2
            node = s1.pop()
            s2.append(node)

            # Push left and right children of removed item to s1
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

            # Print all elements of second stack
        while len(s2) > 0:
            node = s2.pop()
            result.append(node.data)

        return result

    # In order traversal recursive
    def in_order_traversal_rec(self):
        res = []
        if self.left:
            res.extend(self.left.in_order_traversal_rec())
        res.append(self.data)
        if self.right:
            res.extend(self.right.in_order_traversal_rec())
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.in_order_traversal())
print(root.pre_order_traversal())
print(root.post_order_traversal())
