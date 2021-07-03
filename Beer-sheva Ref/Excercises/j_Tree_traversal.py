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

    # Print the tree
    def display(self):
        lines, _, _, _ = self._display_recursive()
        for line in lines:
            print(line)

    def _display_recursive(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root. this is
           a utility function that gets used by the <display()> method for building pretty stdout
           visualization of the binary tree. """

        # No child exists.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child exists.
        if self.right is None:
            lines, n, p, x = self.left._display_recursive()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child exists.
        if self.left is None:
            lines, n, p, x = self.right._display_recursive()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children exist.
        left, n, p, x = self.left._display_recursive()
        right, m, q, y = self.right._display_recursive()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

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


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.display()
print(root.in_order_traversal())
print(root.pre_order_traversal())
print(root.post_order_traversal())
