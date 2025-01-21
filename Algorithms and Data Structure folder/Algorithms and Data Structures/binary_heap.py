class DynamicArray:
    def __init__(self):
        self.data = [None]
        self.length = 0
        
    def insertAt(self, index, value):
        if index < 0 or index > self.length:
            return False
        else:
            if self.length == len(self.data):
                self.resize()
                
            for i in range(self.length -1, index -1, -1):
                self.data[i+1] = self.data[i]
            
            self.data[index] = value
            self.length = self.length + 1
            return True
        
    def resize(self):
        temp = [None] * 2 *len(self.data)
        for i in range(len(self.data)):
            temp[i] = self.data[i]
        self.data = temp
        
        
    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return False
        
        for i in range(index, self.length -1):
            self.data[i] = self.data[i+1]
        self.data[self.length -1] = None
        self.length = self.length - 1
        return True
        

    def printArray(self):
        print(self.data)
        
    def Length(self):
        return self.length
    
    def __getitem__(self,index):
         return self.data[index]

    def setValue(self, index, value):
        self.data[index] = value
    
class Node:
    def __init__(self, priority, val):
        self.value = val
        self.priority = priority

class BinaryHeap:
    def __init__(self):
        self.data = DynamicArray()
    
    def leftChild(self, i):
        return 2*i+1
    
    def rightChild(self, i):
        return 2*i +2
    
    def parent(self, i):
        return (i-1)//2
    
    def isLeaf(self, i):
        if self.leftChild(i) < self.data.Length():
            return False
        else:
            return True
    
    def hasLeftChildOnly(self, i):
        if self.leftChild(i) < self.data.Length() and self.rightChild(i) >= self.data.Length():
            return True
        else:
            return False
    
    def min(self):
        if self.data.Length() > 0:
            return self.data[0]
        else:
            return None
    
    def swap(self, i, j):
        temp = self.data[i]
        self.data.setValue(i, self.data[j])
        self.data.setValue(j, temp)
    
    def upHeapBubbling(self, index):
        if index == 0:
            return
        elif self.data[index].priority < self.data[self.parent(index)].priority:
            self.swap(index, self.parent(index))
            self.upHeapBubbling(self.parent(index))
        else:
            return
    
    def addNode(self, node):
        self.data.insertAt(self.data.Length(), node)
        self.upHeapBubbling(self.data.Length() -1)
        
    def downHeapBubbling(self, index):
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
        
        
    def removeMin(self):
        result = self.data[0]
        self.swap(0, self.data.Length() -1)
        self.data.remove(self.data.Length() -1)
        self.downHeapBubbling(0)
        return result
    
    def Length(self):
        return self.data.Length()
    
    def isEmpty(self):
        if self.Length() == 0:
            return True
        else:
            return False

    def printBinaryHeap(self):
        for node in self.data:
            if node != None:
                print((node.value, node.priority))
        

bh = BinaryHeap()
bh.addNode(Node(0, "A"))
bh.addNode(Node(2, "B"))
bh.addNode(Node(1, "C"))
bh.addNode(Node(3, "D"))
bh.addNode(Node(4, "E"))
bh.addNode(Node(5, "F"))
bh.addNode(Node(6, "G"))
bh.addNode(Node(7, "H"))
bh.addNode(Node(8, "I"))
bh.printBinaryHeap()
print("                ")
minNonde = bh.removeMin()
print((minNonde.value, minNonde.priority))
print("                ")
bh.printBinaryHeap()
print("                ")
minNonde = bh.removeMin()
print((minNonde.value, minNonde.priority))
print("                ")
minNonde = bh.removeMin()
print((minNonde.value, minNonde.priority))
print("                ")
bh.printBinaryHeap()