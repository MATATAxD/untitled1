from pprint import pformat
from queue import Queue


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (
            self.left, self.right)}, indent=1)
        # 结点:(结点的左孩子,结点的右孩子)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:  # self.node is None
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
                        parent_node = parent_node.left

                elif value >= parent_node.value:
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

    def remove(self, values):
        if self.root is None:
            raise IndexError()

    def search(self, value):
        if self.is_empty():
            raise IndexError('空树')
        else:
            node = self.root
            while node and node.value != value:
                if value < node.value:
                    node = node.left
                elif value > node.value:
                    node = node.right

    def is_right(self, node):
        return node == node.parent.right

    def __reassign_nodes(self, node, new_children):  # 找父亲找孩子（逻辑）
        if new_children is not None:  # 如果当前结点子结点非空
            new_children.parent = node.parent  # 子结点和当前结点呼唤位置
        if node.parent is not None:  # 互换位置后，如果当前结点有父结点
            if self.is_right(node):                 # 判断当前结点是否为右侧结点
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def remove(self, value):
        node = self.search(value)  # 返回值对应的结点
        if node is None:
            if node.left is None and node.right is None:  # 没有孩子结点的情况
                self.__reassign_nodes(node, None)  # 交换当前结点和None->当前结点变成空
            elif node.left is None:  # 只有右侧孩子结点
                self.__reassign_nodes(node, node.right)
            elif node.right is None:  # 只有左侧孩子结点
                self.__reassign_nodes(node, node.left)
            else:  # 左右俩孩子都有
                tmp_node = self.get_max(node.left)  # 找到左子树的最大结点
                self.remove(tmp_node.value)  # 删除结点
                node.value = tmp_node.value  # 不改变树结构，只改变当前结点的值

    def preOrder(self, node):  # 前序遍历递归实现
        if not node:
            return None
        print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def preOrder2(self, node):  # 前序遍历用栈实现
        stack = [node]
        while len(stack) > 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def middleOrderTraversal(self, node):  # 中序遍历递归实现
        if not node:
            return None
        self.middleOrderTraversal(node.left)
        print(node.value)  # 中
        self.middleOrderTraversal(node.right)

    def middleOrderTraversal2(self, node):  # 中序遍历栈实现
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.value)
                node = node.right

    def postOrderTraversa(self, node):
        if not node:
            return None
        self.postOrderTraversa(node.left)
        self.postOrderTraversa(node.right)
        print(node.value)

    def postOrderTraversal(self, node):
        if node is None:
            return False
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            elif node.right:
                stack1.append(node.right)

    def levelTraversal(self, root: Node):  # 层序遍历
        if self.is_empty():
            return None
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()  # 返回队列的第一个元素，并从队列中移除
            print(node.value)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.left is not None:
                node = node.left
        return node


l = BinarySearchTree()
l.insert(8, 3, 6, 1, 10)
# l.preOrder2(l.root)
l.middleOrderTraversal2(l.root)
# print(l)
