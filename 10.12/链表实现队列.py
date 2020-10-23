class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class LinkQueue:
    def __init__(self):
        self.first = None
        self.tail  = None
        self.size  = 0

    def push(self,data):  #入队
        new_node = Node(data)
        if self.size == 0:
            self.first = new_node
            self.tail  = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):       #出队
        if self.size == 0:
            raise Exception('空队列')
        else:
            new_node = self.first
            self.first = self.first.next
            new_node.next = None
        self.size -= 1
        return new_node

    def __repr__(self):
        temp = self.first
        string = ''
        while temp:
            string += '{}-->'.format(temp)
            temp = temp.next
        return string + 'END'

if __name__ == '__main__':
    q = LinkQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    print(q)
    q.pop()
    print(q)









