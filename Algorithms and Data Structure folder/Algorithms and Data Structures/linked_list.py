class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self, index, newNode):
        if index == 0:
            if self.length == 0:
                self.head = newNode
            else:
                newNode.next = self.head
                self.head = newNode
                
            self.length = self.length + 1
            return True
            
        elif index > 0 and index < self.length:
            temp = self.head
            i = 0
            while(i < index - 1):
                temp = temp.next
                i = i + 1
                
            newNode.next = temp.next
            temp.next = newNode
            self.length = self.length + 1
            return True
        
        elif index == self.length:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
            self.length = self.length + 1
            return True
        
        else:
            return False
        
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length = self.length - 1
            return True
           
        elif index > 0 and index < self.length:
            temp = self.head
            i = 0
            while(i < index - 1):
                temp = temp.next
                i = i + 1
            if temp.next != None:
                temp.next = temp.next.next
            else:
                temp.next = None
            self.length = self.length - 1
            return True

        else:
            return False
        
    
    def printLinkedList(self):
        temp = self.head
        while(temp != None):
            print(temp.value)
            temp = temp.next

"""
sl = SingleLinkedList()
sl.insert(0, Node("A"))
sl.insert(1, Node("B"))
sl.insert(2, Node("C"))
sl.insert(3, Node("D"))
sl.printLinkedList()
print("=====")
sl.insert(2, Node("X"))
sl.printLinkedList()
sl.remove(2)
print("=====")
sl.printLinkedList()
"""

class NodeEx:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  
    
    def insertAt(self, index, newNode):
        if index == 0:
            if self.length == 0:
                self.head = newNode
                self.tail = newNode
            else:
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
                
            self.length = self.length + 1
            return True
            
        elif index > 0 and index < self.length:
            temp = self.head
            i = 0
            while(i < index - 1):
                temp = temp.next
                i = i + 1
                
            newNode.next = temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next = newNode
            self.length = self.length + 1
            return True

        elif index == self.length:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.length = self.length + 1
            return True
        
        else:
            return False
    
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length = self.length - 1
            return True
           
        elif index > 0 and index < self.length:
            temp = self.head
            i = 0
            while(i < index - 1):
                temp = temp.next
                i = i + 1
            if temp.next != None:
                temp.next = temp.next.next
                temp.next.prev = temp
            else:
                self.tail = temp
                temp.next = None
            self.length = self.length - 1
            return True

        else:
            return False 


    def swap(self, index1, index2):
        temp = index1
        index1 = index2
        index2 = temp     
    

    def reverse(self):
        self.head = self.tail
        for i in range(self.length):
            self.head = self.tail.prev
            

 
        
        
    def printLinkedList(self):
        temp = self.head
        while(temp != None):
            print(temp.value)
            temp = temp.next


dLList = DoubleLinkedList()
dLList. insertAt(0, Node(1))
dLList. insertAt(1, Node(3))
dLList. insertAt(2, Node(5))
dLList. insertAt(2, Node(2))
dLList. insertAt(0, Node(0))
dLList. insertAt(4, Node(4))
print('First Print Results\n')
dLList. printLinkedList()
dLList. reverse()
print('Second Print Results\n')
dLList. printLinkedList()
dLList. swap(0, 5)
dLList. swap(1, 4)
print('Third Print Results\n')
dLList. printLinkedList()
dLList.remove(0)
dLList.remove(4)
dLList.remove(1)
print('Fourth Print Results\n')
dLList. print()

