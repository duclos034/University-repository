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

class Stack():
    def __init__(self):
        self.array = DynamicArray()
    def push(self, value):
        self.array.insertAt(self.array.length(), value)
    
    def pop(self):
        self.array.remove(self.array[0])
        return 0  
      
    def top(self):
        print(self.array[0])

    
    def isEmpty(self):
        if self.array[0] == None:
              return True
        else:
            return False
        
    def length(self):
        print(DynamicArray.length)
    
    def printStack(self):
        return 0 
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
          
              

        

