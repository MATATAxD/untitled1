class Node:
    def __init__(self,data):
        self.data = data
        self.next = Node

    def __repr__(self):
        return 'Node({})'.format(self.data)

def twolists(l1:Node,l2:Node):
    dummy = Node(0)
    cur = dummy
    while l1 or l2:
        if l2.data < l1.data:
            cur.next = Node(l2.data)
            l2 = l2.next
        else:
            cur.next = Node(l1.data)
            l1 = l1.next
        cur = cur.next
        if l1 is None:
            cur.next = l2
            break
        if l2 is None:
            cur.next = l1
            break
    return dummy.next


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
    # print(twolists())

