from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)

def swapPairs(head: Node) -> List:
    dummy = Node(0)
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
        slow = pre.next
        fast = pre.next.next
        pre.next = fast
        slow.next = fast.next
        fast.next = slow
        pre = pre.next.next
    return dummy.next

def print_list(head):
    curr=head
    while curr:
        print(curr.data)
        curr = curr.next



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
    node7.next = None
    print(print_list(node1))
