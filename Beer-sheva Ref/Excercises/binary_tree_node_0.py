



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
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

def find_val_rec(node,val):
    if node is None:
        return False
    if node.data == val:
        return True
    if node.data < val:
        return find_val(node.right, val)
    else:
        return find_val(node.left, val)

if __name__ == '__main__':
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(8)
    print(root.findval(7))
    print(root.findval(14))
    print(find_val(root, 3))
