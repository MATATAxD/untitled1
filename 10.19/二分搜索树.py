from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({'%s' % (self.value): (
            self.left, self.right)}, indent=1)


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def __insert(self, value):
        node = Node(value, None)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if value > parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node.right = node

                elif value <= parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right

            node.parent = parent_node

    def insert(self,*values):
        for value in values:
            self.__insert(value)
        return self


    def preOrder(self, node):
        stack = []
        while len(stack) > 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def midOrder(self, node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            while len(stack) > 0:
                node = stack.pop()
                print(node.value)
                node = node.right

    def postOrder(self, node):
        if node is None:
            return False
        stack1 = []
        stack2 = []
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

l = BST()
l.insert(8, 3, 6, 1, 10)
