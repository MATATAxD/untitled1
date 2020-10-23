class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class Linklist:
    def __init__(self,top):
        self.top = None
        self.size = 0


    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise Exception('空栈')
        else:
            new_node = self.top
            self.top = new_node.next
            new_node.next = None
            self.size -= 1
        return new_node

    def is_empty(self):
        return self.top is None


    def sizeof(self):
        return self.size


    def __repr__(self):
        temp = self.top
        string =''
        while temp:
            string += '{}-->'.format(temp)
            temp = temp.next
        return string +'END'

if __name__ == '__main__':
    stack = Linklist(10)
    for i in range(10):
        stack.push(i)
    print(stack)
    for i in range(5):
        stack.pop()
    print(stack)
    print(stack.sizeof())
    print(stack.size)
    print(stack.is_empty())

