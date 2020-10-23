class PriorityQueue:    #用堆实现
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self,data):
        self.array.append(data)
        self.size += 1
        self.hepify_up()

    def dequeue(self,data):
        if self.size <= 0:
            raise Exception("空队列")
        remove_value = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size -= 1
        self.heapify_down()
        return remove_value


    def hepify_up(self):
        child_index = self.size - 1
        parent_index = (child_index - 1) >>1
        new = self.array[child_index]
        while child_index > 0 and new >self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1) >> 1    #父节点向上移动
        self.array[child_index] = new

    def hepify_dowm(self):
        total_index = self.size - 1
        index = 0
        while True:
            maxvalue_index =index
            if 2 * index + 1 <= total_index and self.data_list[2 * index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1     #如左孩子结点大于当前结点，最大值索引等于左孩子索引
            if 2 * index + 2 <= total_index and self.data_list[2 * index + 2]  >self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2     #如右孩子结点大于当前结点，最大值索引等于右孩子索引
            if maxvalue_index == index:
                break
            self.swap(index,maxvalue_index)          #交换最大值和当前值
            index = maxvalue_index                      #当前值等于这一轮的最大值结点

if __name__ =='__main__':
    hh=PriorityQueue()
    hh.enqueue(1)
    hh.enqueue(2)
    hh.enqueue(3)
    hh.enqueue(4)
    hh.enqueue(5)
    print(hh.array)



