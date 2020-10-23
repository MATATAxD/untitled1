class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent_index(self, index):
        if index <= 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):  # 交换元素
        # 交换
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def pop(self):
        remove_data = self.data_list[0]     #找到堆顶元素
        self.data_list[0] = self.data_list[-1]    #替换最后一个元素到堆顶
        del self.data_list[-1]                #删除最后一个元素
        self.heapify(0)               #从顶端堆化
        return remove_data        #返回删除的元素

    def heapify(self,index):
        total_index =len(self.data_list) -1  #数组的长度
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



if __name__ == '__main__':
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    # print(heap.data_list)
    print(heap.data_list)