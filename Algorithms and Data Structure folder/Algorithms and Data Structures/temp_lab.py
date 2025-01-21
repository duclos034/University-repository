class DynamicArray:
    def __init__(self):
        self.data = [None] * 1
        self.length = 0

    def insertAt(self, index, value):
        if index > self.length or index < 0:
            return False
        self.length = self.length + 1
        if self.length == len(self.data):
            self.resize()
        for i in range(self.length, index, -1):
                     self.data[i] = self.data[i - 1]
        self.data[index] = value
        return True
    

    def remove(self, index):
        if index > self.length - 1 or index < 0:
            return False
        self.length = self.length - 1
        self.data[index] = None
        for i in range(index, self.length + 1):
            self.data[i] = self.data[i + 1]
            return True
         
                   
    def length(self):
        return self.length
    
    def printArray(self):
        print(self.data)

    def resize(self):
        filler = [None] * (len(self.data) * 2)
        for i in range(0, self.length):
            filler[i] = self.data[i]
        self.data = filler

    def getItem(self, index):
          return self.data[index]
    
    def size(self):
         return len(self.data)
    

class Stack():
    def __init__(self):
        self.array = DynamicArray()

    def push(self, value):
        self.array.insertAt(self.array.length, value)
    
    def pop(self):
        temp = self.array.getItem(self.array.length -1)
        self.array.remove(self.array.length -1)
        return temp
      
    def top(self):
        print(self.array[0])

    def isEmpty(self):
        if self.array.length == 0:
              return True
        else:
            return False
        
    def length(self):
        return self.array.length + 1
    
    def printStack(self):
        self.array.printArray()


class Queue():
    def __init__(self):
        self.array = DynamicArray()
        self.first = 0

    def enqueue(self, value):
        #impletment insert
        self.array.insertAt(self.array.length, value)
          
    def dequeue(self):
          #call remove from dynamic
          self.first = 0
          temp = self.array.getItem(self.first)
          self.array.remove(self.first)
          self.first = (self.first + 1) % self.array.size()
          return temp
      
    def length(self):
        return self.array.length + 1
        
    def front(self):
        return self.array.getItem(self.first) 
     
    def isEmpty(self):
        if self.array.length == 0:
              return True
        else:
            return False
    def printArray(self):
         self.array.printArray()         

a = DynamicArray()

a.insertAt(5, 5)
a.printArray()


