class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
    def __str__(self) -> str:
        return ', '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) == 0
    def insert(self,data):
        self.queue.append(data)
    def delete(self):
        try:
            maxvalue = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[maxvalue]:
                    maxvalue = i
            items = self.queue[maxvalue]
            del self.queue[maxvalue]
            return items
        except IndexError:
            print('Index Error !!!')
            exit()

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print("Queue: ", myQueue)
    while not myQueue.isEmpty():
        print("Popped out:", myQueue.delete())
print("Coded by Qureshi Safdar Ali, Roll no: 536")

