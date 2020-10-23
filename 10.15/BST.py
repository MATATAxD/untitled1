from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.right = None
        self.left = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({'%s '% (self.data):(self.left,self.right)},indent=1)


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
        new_node = Node(value,parent= None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.data:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values):  # 不定长参数
        for value in values:
            self.__insert(value)
        return self

    def search(self,value):
        if self.is_empty():
            raise  Exception('空树')
        else:
            node = self.root
            while node and node.value != value:
                if value < node.left:
                    node = node.left
                elif value > node.value:
                    node = node.right



    def is_right(self,node):
        return node == node.parent.right

    def __reassign(self,node,new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is None:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def remove(self,value):
        node = self.search(value)
        if node is None:
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

ll = BST()
ll.insert(1,2,3,4,5,6)
ll.remove(2)
print(ll)



