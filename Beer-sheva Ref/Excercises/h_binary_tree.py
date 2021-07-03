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

    # findval method to compare the value with nodes
    def findval(self, lkpval) -> bool:
        if lkpval < self.data:
            if self.left is None:
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return False
            return self.right.findval(lkpval)
        else:
            return True

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

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(8)
    root.display()
    print(root.findval(7))
    print(root.findval(14))
