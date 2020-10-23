class Queue:
    def __init__(self):
        self.entries = []
        self.size =0


    def __rapr__(self):
        printed = '<' + str(self.entries)[1:-1] + '>'
        return printed

    def enqueue(self,data): #入队
        self.entries.append(data)
        self.size += 1

    def dequeue(self):     #出队
        temp = self.entries[0]
        self.entries = self.entries[1:]
        self.size -= 1
        return temp

    def get(self,index):
        temp = self.entries[0]
        pass

    def sizeof(self):
        return self.size

    def reversed(self):
        pass








