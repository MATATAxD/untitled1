from typing import List
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)

class Linklist:
    def __init__(self):
        self.head = None

    def insert_head(self, data):  # 头部插入结点
        new_node = Node(data)  # 创建新结点
        if self.head is not None:  # 如果头部结点不为空
            new_node.next = self.head  # 头部插入新结点
        self.head = new_node  # 头部结点重置

    def append(self, data):  # 尾部插入
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    def __repr__(self):  # 打印链表
        current = self.head
        string_repr = ''
        while current is not None:
            string_repr += '{}-->'.format(current)
            current = current.next
        return string_repr + 'END'

    def insert(self, i, data):  # 中间插入结点
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            j = 1
            pre = temp
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            new_node = Node(data)
            pre.next = new_node
            new_node.next = temp

    def linklist(self, object: List):  # 类型注解 object:list类型    插入一个列表到链表
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            new_node = Node(i)
            temp.next = new_node
            temp = temp.next

    def delete_head(self):  # 删除头结点
        temp = self.head
        if self.head is not None:
            self.head = self.head.next
        #     temp.next = None
        # return temp

    def delete_tail(self):
        temp = self.head
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
        else:
            return '空链表'

ll = Linklist()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.append(5)
ll.insert(2, 3)
# ll.linklist([1,2,3,4])
ll.delete_head()
# ll.delete_tail()
print(ll)
