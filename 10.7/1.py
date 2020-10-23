from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        temp = self.head  # 准备遍历先找到链表头
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception('索引越界')
        elif self.size == 0:  # 空链表
            self.head = new_node
            self.tail = new_node
        elif index == 0:  # 头部插
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:  # 尾部插
            self.tail.next = new_node
            self.tail = new_node
        else:  # 中间插
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def __repr__(self):
        temp = self.head
        string = ''
        while temp is not None:
            string += '{}-->'.format(temp)
            temp = temp.next
        return string + 'END'

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception('索引越界')
        if index == 0:    #删除头部
            remove_node = self.head
            self.head = self.head.next
        elif index == self.size-1:   #删除尾部
            prev = self.get(index-1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:                     #中间删除
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next
        self.size-=1
        return remove_node

    def reversed(self):
        pre = None
        curr = self.head
        while curr:
            temp = curr.next
            if pre is None:
                curr.next = pre
            else:
                curr.next = pre
            pre = curr
            curr = temp
        self.head = pre





ll = Linklist()
ll.insert(0, 1)
ll.insert(1, 2)
ll.insert(2, 3)
# ll.remove(2)
# ll.reversed()
print(ll)
