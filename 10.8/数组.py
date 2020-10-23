class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity  # 数组的长度 列表
        self.size = 0  # 数组的有效元素多少

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError('数组越界')
        if index >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2   #创建新数组
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

if __name__ =='__main__':
    array =Array(10)
    array.insert(0,1)
    print(array.size)
    array.insert(1, 1)
    print(array.size)
    array.insert(2,2)
    print(array.size)