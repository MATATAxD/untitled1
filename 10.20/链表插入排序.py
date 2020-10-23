from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


def insert(head:Node):
    dummy = Node(0)
    pre = dummy
    cur = head
    while cur is not None:
        temp = cur.next
        while pre.next is not None and pre.next.data < cur.data:
            pre = pre.next
        cur.next =pre.next
        pre.next =cur
        cur = temp
        pre =dummy
    return dummy.next
