class FixedSizeArray:
    def __init__(self, N): 
        self.data = [None]*N
        self.length = 0
        self.capacity = N


    def insertAt(self, index, value): 
       
        if index > self.capacity or index < 0:
            return False
        self.length = self.length + 1
        for i in range(self.length, index, -1):
                     self.data[i] = self.data[i - 1]
        self.data[index] = value
        return True


    def remove(self, index): 
        if index > self.capacity or index < 0:
            return False
        self.data[index] = None
        for i in range(index, self.length + 1):
            self.data[i] = self.data[i + 1]
        return True
        

    def getItem(self, index):
        return self.data[index]
    

    def printArray(self): 
        print(self.data)


    def length(self): 
        return self.length
    

class Dequeue:
    def __init__(self, n):
         self.array = FixedSizeArray(n)
         self.first = 0
         self.last = self.array.capacity -1 


    def add_first(self,e):
        
        self.array.insertAt(self.first, e)
    

    def add_last(self,e):
        self.array.insertAt(self.array.capacity - 1, e  )
    

    def delete_first(self):
        if self.first == None:
             return False
        temp = self.array.getItem(self.first)
        self.array.remove(self.first)
        return temp
    

    def delete_last(self):
        if self.last == None:
            return False
        temp = self.array.getItem(self.last)
        self.array.remove(self.last)
        return temp
        

    def first(self):
         return self.array.getItem(self.first)
    

    def last(self):
         return self.array.getItem(self.last)
    

    def printDequeue(self):
        self.array.printArray()
    

    def isEmpty(self):
        if self.array.length == 0:
              return True
        else:
            return False
    def length(self):
        return self.array.length + 1
D = Dequeue(10)

D.delete_last()
D.add_last(50)
D.add_first(2)
D.delete_last()
D.printDequeue()
D.add_first(10)
D.add_first(100)
D.add_last(1)
D.delete_last()
D.delete_first()
D.length()
D.printDequeue()