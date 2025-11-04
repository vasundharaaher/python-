"""
# Queue
Fist In First Out

Oprations on Queue
Enqueue : Adding element 
Dequeue : Removing Elememt
Size : tell no of elements in queue
Is Empty : Queue empty
front : Oldest element ( from where element get remove)
Rear : Newest element ( From where element get added ) 

"""



"""

class QueueUsingList:

    def __init__(self):
        self.__queue =[]

    def size(self):
        return len(self.__queue)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self,data):
        self.__queue.append(data)
        return f"We have added {data} to the Queue"

    def dequeue(self):
        if self.size() == 0:
            return "Queue is Emapty, cannot dequeue"
        data = self.__queue.pop(0)
        return f"We have removed element {data} from Queue"

    def front(self):
        if self.size() == 0:
            return "Queue is Emapty No front is present"
        
        data = self.__queue[0]
        return f"Front is {data}"
    
    def rear(self):
        if self.size() == 0:
            return "Queue is Emapty No Rear is present"
        rear_ix = self.size()
        data = self.__queue[rear_ix -1]
        return f"Rear : {data}"
        


Q = QueueUsingList()

print(Q.isEmpty())

print(Q.enqueue(10))
print(Q.enqueue(20))
print(Q.enqueue(30))
print(Q.enqueue(40))
print(Q.enqueue(50))

print(Q.front())
print(Q.rear())
print(Q.size())

print(Q.dequeue())
print(Q.dequeue())

print(Q.isEmpty())

print(Q.front())
print(Q.rear())
print(Q.size())

"""


""" Queue using link list """

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def size(self):
        return self.len
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self, data):
        NewNode = Node(data)
        self.len += 1
        if (self.head is None):
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = NewNode    # Next of Tail Old tail (node) is now new node
            self.tail = NewNode     # Newly add node become new tail
        return f"Added {data} to the Queue"
    
    def front(self):
        if(self.isEmpty()):
            print("Queue is Empty, cannot display front")
            return
        
        return f"Front : {self.head.data}"
    
    def rear(self):
        if(self.isEmpty()):
            print("Queue is Empty, cannot display rear")
            return
        
        return f"Rear : {self.tail.data}"
    
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty, Cannot Dequeue")
            return
        
        self.len -= 1
        deldata = self.head.data
        self.head = self.head.next

        if(self.head == None):  # When there is only one element in queue
            self.tail = None

        return f"Data {deldata} is deleted from front"
    


Q = QueueUsingLinkedList()

print(Q.isEmpty())

print(Q.enqueue(10))
print(Q.enqueue(20))
print(Q.enqueue(30))
print(Q.enqueue(40))
print(Q.enqueue(50))

print(Q.front())
print(Q.rear())
print(Q.size())

print(Q.dequeue())
print(Q.dequeue())

print(Q.isEmpty())

print(Q.front())
print(Q.rear())
print(Q.size())