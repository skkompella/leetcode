class MyCircularQueue:
    queue = []
    write = 0
    read = 0
    capacity = 0
    def __init__(self, k: int):
        self.queue = [None] * k
        self.write = 0
        self.read = 0
        self.capacity = k
    def enQueue(self, value: int) -> bool:
        if self.isFull() == True:
            return False
        self.queue[self.write] = value
        self.write = (self.write + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() == True:
            return False
        self.queue[self.read] = None
        self.read = (self.read + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.read]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.write - 1) % self.capacity]

    def isEmpty(self) -> bool:
        if self.write == self.read:
            if self.queue[(self.write+1) % self.capacity] == None and self.queue[(self.write-1)%self.capacity] == None:
                return True
        return False
        # for i in self.queue:
        #     if i != None:
        #         return False
        # return True

    def isFull(self) -> bool:
        if self.write == self.read:
            if self.queue[(self.write+1) % self.capacity] != None and self.queue[(self.write-1)%self.capacity] != None:
                return True
        return False

        # for i in self.queue:
        #     if i == None:
        #         return False
        # return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
