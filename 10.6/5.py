from typing import List
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class Linklist:
    def __init__(self):
        self.head = None


    def insert_head(self,data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def append(self,data):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    def __repr__(self):
        cuurent = self.head
        string = ''
        while cuurent is not None:
            string += '{}-->'.format(cuurent)
            cuurent = cuurent.next
        return string + 'END'


    def insert(self,i,data):
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
                j+=1
            new_node = Node(data)
            pre.next = new_node
            new_node.next = temp

    def linklist(self,object:List):
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            new_node = Node(i)
            temp.next = new_node
            temp = temp.next

    def delete_head(self):
        temp = self.head
        if self.head is not None:
            self.head = self.head.next

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
# ll.insert_head(1)
# ll.insert_head(2)
# ll.insert_head(3)
# ll.insert_head(4)
# ll.append(5)
# ll.insert(2, 3)
ll.linklist([1,2,3,4])
# ll.delete_head()
# ll.delete_tail()
print(ll)


