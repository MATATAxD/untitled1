from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


    def __repr__(self):
        return 'Node({})'.format(self.data)

def removenode(head,val:int):
    if head.val == val:
        return head.next
    pre = head
    cur = head.next
    while cur and cur.next != val:
        pre = cur
        cur = pre.next
    if cur:
        pre.next = cur.next
    return head

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    print(removenode(node1,1))
