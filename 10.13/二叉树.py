class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    def get_parent(self,data):   #获取父节点
        if self.root.data == data:
            return None
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left.data == data:    #节点的左子树为寻找的点
                return pop_node                #返回该节点
            if pop_node.right.data == data:        #节点的右子树为寻找的点
                return pop_node                       #返回该节点
            if pop_node.left:                   #添加到temp
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        return None



if __name__ == '__main__':
    tre = Tree()
    tre.add(1)
    tre.add(2)
    tre.add(3)
    tre.add(4)
    tre.add(5)
    tre.add(6)
    tre.add(7)
    print(tre.get_parent(3))
