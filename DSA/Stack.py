'''
Stack Implementation : Using In-Built Python List
'''
"""
class StackUsingList:
    def __init__(self):
        self.__stack = []       # it is important to make it private for the functinality purpose

    def push(self,data):
        self.__stack.append(data)
        print(f"Push {data} into Stack")

    def size(self):
        return len(self.__stack)
    
    def is_empty(self):
        '''
        if(len(self.stack)==0):
            return True
        else:
            return False
        '''
        return len(self.__stack) == 0
    
    def top(self):
        # return self.stack 
        if(self.is_empty()):
            print("Stack is Empty , No top element")
            return None 
        #return self.stack[len(self.stack)-1]

        return self.__stack[-1]
    def pop(self):
        if(self.is_empty()):
            print("Stack is Empty , cann't pop")
            return None
        return self.__stack.pop()

mystack= StackUsingList()

print(mystack.is_empty())
print(mystack.push(1))
print(mystack.push(2))
print(mystack.push(3))
print(mystack.push(4))

print(mystack.is_empty())
print(mystack.pop())
print(mystack.pop())
print(mystack.size())
print(mystack.top())

mystack.__stack

"""

"""Stack using Link List"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackUsingLinkList:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self,data):
        NewNode = Node(data)
        self.len += 1
        if(self.head==None):
            self.head=NewNode
            return f"Added {data} to the stack"
        
        NewNode.next = self.head
        self.head = NewNode
        return f"Added {data} to the stack"

    def top(self):
        if(self.head is None or self.size == 0):
            return "Stack is underflow"
        
        return self.head.data

    def pop(self):
        if(self.head is None or self.len == 0):
            return "Stack is underflow can not pop element"
        
        dataTop=self.head.data
        self.head= self.head.next
        self.len -= 1
        return dataTop
    
    def size(self):
        return self.len
    
    def isEmpty(self):
        return self.len==0
        

    
mystack= StackUsingLinkList()

print(mystack.isEmpty())
print(mystack.push(1))
print(mystack.push(2))
print(mystack.push(3))
print(mystack.push(4))

print(mystack.isEmpty())
print(mystack.pop())
print(mystack.pop())
print(mystack.size())
print(mystack.top())


