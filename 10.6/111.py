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
        self.tail = None
        self.size = 0
