class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


    def reversed(self):
        pre = None
        cur = self.head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        self.head = pre

