from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)


class BST:
    def __init__(self, root):
        self.root = root

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def __insert(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node.left = parent_node.left
                elif value >= parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node.right = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values):
        for value in values:
            self.__insert(value)
        return self
    def search(self,value):
        if self.is_empty():
            raise IndexError('空')
        else:
            node=self.root
            while node and node.value !=value:
                node =node.left if value < node.value else node.right
            print(node)
            return node

    def __reassign_nodes(self,node,new_children):
        if new_children is not None:
            new_children.parent=node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right =new_children
            else:
                 node.parent.left = new_children
        else:
                node.parent.left = new_children

    def remove(self,value):
        node=self.search(value)
        if node is not None:
            if node.left is None and node.right is None:
                self.__ressign_noods(node,None)
            elif node.left is None:
                self.__ressign_nodes(node,node.right)
            elif node.right is None:
                self.__ressign_nodes(node,node.left)
            else:
                tmp_node =self.get_max(node.left)
                self.remove(tmp_node.value)
                node.value =tmp_node.value

    def get_max(self,node=None):
        if node is None:
            node =self.root
        if not self.is_empty():
            while node.right is not None:
                node =node.right
        return node



if __name__ == "__main__":
   bst = BST().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
   print(bst)
   bst.search(3)
   bst.remove(1)
   print(bst)
