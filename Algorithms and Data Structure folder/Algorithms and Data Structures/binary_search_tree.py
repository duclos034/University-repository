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
                   
    def Length(self):
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
   
    def getSize(self):
        return len(self.data)


class Queue():
    def __init__(self):
        self.array = DynamicArray()
        self.first = 0

    def enqueue(self, value):
        #impletment insert
        self.array.insertAt(self.array.length, value)
          
    def dequeue(self):
          #call remove from dynamic
          
          temp = self.array.getItem(self.first)
          self.array.remove(self.first)
          #self.first = (self.first + 1) % self.array.size()
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


class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    
    
    def addNode(self, node):
        if self.root == None:
            self.root = node
        else:
            temp = self.root
            bLeft = True
            while temp != None:
                if temp.value >= node.value:
                    if temp.left != None:
                        temp = temp.left
                    else:
                        break
                else:
                    if temp.right != None:
                        temp = temp.right
                    else:
                        bLeft = False 
                        break

            if bLeft == True:
                temp.left = node
            else:
                temp.right = node
            node.parent = temp

    def remove(self, node):
        if node.left == None and node.right == None:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left == None or node.right == None:
            child = None
            if node.left != None:
                child = node.left
            else:
                child = node.right
            if node  == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        else:
            temp = node.right
            while temp.left != None:
                temp = temp.left
            node.value = temp.value
            if temp == temp.parent.left:
                temp.parent.left = None
            else:
                temp.parent.right = None 


    def search(self, value):
        temp = self.root
        placeholder = temp.root

        while temp != None:
            if temp.value == value:
                return True
                
            elif temp.value > value:
                temp = temp.left

            elif temp <= value:
                temp = temp.right
            
            elif temp == None:
                temp = placeholder 
        return False
    
    def depth(self):
        return 0
    
    
    def children(self):
        return 0
    
    
    def parent():
        return 0
    

    def inOrderTraversal(self, node):
        if node != None:
            self.inOrderTraversal(node.left)
            print(node.value)
            self.inOrderTraversal(node.right)


    def preOrderTraversal(self, node):
        if node != None:
            print(node.value)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)
    

    def postOrderTraversal(self, node):
        if node != None:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.value)
        
    def printTreeLevelByLevel(self):
        q = Queue()
        q.enqueue(self.root)
        while(q.isEmpty() == False):
            temp = q.dequeue()
            print(temp.value)
            if temp.left != None:
                q.enqueue(temp.left)
            if temp.right != None:
                q.enqueue(temp.right)
    

#write a main and put the nodes into it. 
bst = BST()
bst.addNode(Node(50))
bst.addNode(Node(45))
bst.addNode(Node(46))
bst.addNode(Node(47))
bst.addNode(Node(52))
bst.addNode(Node(59))
bst.addNode(Node(51))
bst.addNode(Node(48))

bst.inOrderTraversal(bst.root)
print("========")
bst.preOrderTraversal(bst.root)
print("========")
bst.postOrderTraversal(bst.root)
print("========")
bst.printTreeLevelByLevel()