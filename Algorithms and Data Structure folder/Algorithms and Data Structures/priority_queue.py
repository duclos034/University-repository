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

    def __getitem__(self,index):
        return self.data[index]



class Node:
    def __init__(self,priority, val):
        self.value = val
        self.priority = priority

class BinaryHeap():
    def __init__(self):
        self.data = DynamicArray()

    

    def leftChild(self, i):
        return self.data[2*i+1]


    def rightChild(self,i):
        return self.data[2*i+2]
    

    def parent(self,i):
        return self.data[(i-1)//2]
    

    def isLeaf(self, i):
        if self.leftChild(i) < self.data.length():
            return False
        else:
            return True

    def hasLeftChildOnly(self, i):
        if self.leftChild(i) < self.data.length() and self.rightChild(i) >= self.data.length():
            return False
        else:
            return True

    def min(self):
        if self.data.length() > 0:
            return self.data[0]
        else:
            return None

    def swap(self,i,j):
        temp = self.data[i] = self.data[j]
        self.data[i], self.data[j] = self.data[j], self.data[i]


    def upHeapBubbling(self, index):
        if index == 0:
            return 
        elif self.data[index].priority < self.data[self.parent(index)].priority:
            self.swap(index, self.parent(index))
            self.upHeapBubbling(self.parent(index))
        else:
            return

    
    def downHeapBubbling(self,index):
        if self.isLeaf(index) == True:
            return 
        elif self.hasLeftChildOnly(index) == True:
            if self.data[index].priority > self.data[self.leftChild(index)].priority:
                self.swap(index, self.leftChild(index))
                self.downHeapBubbling(self.leftChild(index))
        else:
            if self.data[self.leftChild(index)].priority < self.data[self.rightChild(index)].priority:
                self.swap(index, self.leftChild(index))
                self.downHeapBubbling(self.leftChild(index))
            else:
                self.swap(index, self.rightChild(index))
                self.downHeapBubbling(self.rightChild(index))
            



    def addNode(self,node):
        self.data.insertAt(self.data.length(), node)
        self.upHeapBubbling(self.data.length() - 1)


    def removeMin(self):
         result = self.data[0]
         self.swap(0, self.data.length() - 1)
         self.data.remove(self.data.length() - 1)
         self.downHeapBubbling(0)

    def length(self):
        return self.data.length()
    

    def isEmpty(self):
        if self.length() == 0:
            return True
        else:
             return False
        

    def printBinaryHeap(self):
        print(self.data.printArray())        


bh = BinaryHeap()
bh.addNode(Node(0, 'A'))
bh.addNode(Node(0, 'B'))
bh.addNode(Node(0, 'C'))
bh.addNode(Node(0, 'D'))
bh.addNode(Node(0, 'E'))
bh.addNode(Node(0, 'F'))
bh.addNode(Node(0, 'G'))
bh.addNode(Node(0, 'H'))
bh.addNode(Node(0, 'I'))
bh.printBinaryHeap()
print(bh.removeMin())
bh.printBinaryHeap()
