from pprint import pformat
class Node:
    def __init__(self,parent,value):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({'%s' %(self.value):(self.right,self.left)},indent= 1)

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


    def __insert(self,value):
        new_node = Node(value,None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = new_node
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self,*values):
        for value in values:
            self.__insert(value)
        return self

    def search(self,value):
        if self.is_empty():
            raise Exception('空树')
        else:
            node = self.root
            while node and node.value != value:
                if value < node.value:
                    node = node.left
                elif value > node.value:
                    node = node.right

    def is_right(self,node):
        return  node == node.parent.right

    def __reassign(self,node,new_children):
        if new_children is None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children


    def remove(self,value):
        node = self.search(value)
        if node is None:
            if node.left is None and node.right is None:
                self.__reassign(node,None)
            elif node.left is None:
                self.__reassign(node,node.right)
            elif node.right is None:
                self.__reassign(node,node.left)
            else:
                tmp_node = self.get_max(node.left)
                self.remove(tmp_node.value)
                node.value = tmp_node.value

    def preOrder(self,node):
        if not node:
            return None
            print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def preOrder2(self,node):
        stack = []
        while len(stack) > 0 :
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def midleOrder(self,node):
        if not node:
            return None
        self.midleOrder(node.left)
        print(node.value)
        self.midleOrder(node.right)

    def midleOrder2(self,node):
        stack = []
        while node or len(stack)> 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop(node)
                print(node.value)
                node = node.right

l = BST()
l.insert(1,2,3,4,5,6,7,8)






