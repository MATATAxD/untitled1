from typing import List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return f'None({self.data})'


class LinkList:
     def __init__(self):
         self.head=Node
         self.tial=None
         self.size=0
