from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'None ({self.data})'


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr

    def insert(self, index, data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception('索引越界')
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size - 1:
            self.tail.next = new_node
            self.tail = new_node
        else:
            pre = self.get(index - 1)
            new_node.next = pre.next
            pre.next = new_node
        self.size += 1

    def delete(self, index):
        if index < 0 or index > self.size:
            raise Exception('索引越界')
        elif index == 0:
            remove_node = self.head
            self.head = self .head.next
        elif index == self.size - 1:
            pre = self.get(index - 1)
            remove_node = pre.next
            pre.next = None
            self.tail = pre
        else:
            pre = self.get(index - 1)
            remove_node = pre.next
            pre.next = pre.next.next
        self.size -= 1

    def reverse(self):
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

    def __repr__(self):
        curr = self.head
        result = ''
        while curr:
            result += f"{curr}-->"
            curr = curr.next
        return result + 'END'


if __name__ == '__main__':
    ll = LinkList()
    ll.insert(0, 1)
    ll.insert(1, 2)
    ll.insert(2, 3)
    print(ll)
    ll.delete(0)
    print(ll)
