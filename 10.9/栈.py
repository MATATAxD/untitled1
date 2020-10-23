class stack:
    def __init__(self, limit=10):
        self.stack = []
        self.size = 0

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
        else:
            raise Exception('空栈')
        return temp

    def peek(self):   #返回第一个
        if self.stack:
            return stack.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return self.size


if __name__ =='__main__':
    a = stack(10)
    # stack.pop()
    print(a)
