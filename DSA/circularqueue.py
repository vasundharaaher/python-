class CircularOueue:
    def __init__(self, size):
        self.size = size
        self.items = [None]*size
        self.front = self.rear = -1

    def enqueue(self, value):
        if((self.rear + 1) % self.size  == self.front) :
            print("Queue is full....")
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
            print(self.items[self.rear])
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
            print(self.items[self.rear])

    def dequeue(self):
        if(self.rear == -1):
            print("Queue is empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size

cq = CircularOueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()