class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val



class HashTable:
    def __init__(self, n):
        self.data = [None] * n
        self.length = 0


    def hashCode(self, key):
        temp = key
        result = 0b1111111 
        while temp != 0:
            m = temp % 10
            result = result ^ m 
            temp = temp//10

        return result % len(self.data)


    def add(self, node):
        index = self.hashCode(node.key)
        if self.data[index] == None:
            self.data[index] = node
        else:
            if isinstance(self.data[index], list):
                self.data[index].append(node)
            else:
                temp = []
                temp.append(self.data[index])
                temp.append(node)
                self.data[index] = temp
    
    
    def remove(self, key):
        index = self.hashCode(key)
        if self.data[index] == None:
            return True
        else:
            if isinstance(self.data[index], list):
                for i in range(len(self.data[index])):
                    if self.data[index][i].key == key:
                        self.data[index].pop(i)
                        break

            else:
                if self.data[index].key ==key:
                    self.data[index] = None
    

    def update(self, key, newValue):
        index = self.hashCode(key)
        if self.data[index] == None:
            return
        else:
            if isinstance(self.data[index], list):
                for i in range(len(self.data[index])):
                    if self.data[index][i].key == key:
                        self.data[index][i] = Node(key, newValue)
                        break
            else:
                if self.data[index].key == key:
                    self.data[index] = Node(key, newValue)

    
    def printHashTable(self):
        for node in self.data:
            if isinstance(node, list):
                print("List inside the hashtable")
                for item in node:
                    print(item.key, item.value)
                print("List printing is done!!")
            elif node != None:
                print(node.key, node.value)
            else:
                print("Empty Index :(")
    

    def get(key):
        return key
    

    def length():
        return 0 
    

ht = HashTable(20)
ht.add(Node(12, "A"))
ht.add(Node(11, "B"))
ht.add(Node(112, "C"))
ht.add(Node(121, "D"))
ht.add(Node(120, "E"))
ht.add(Node(2, "F"))
ht.add(Node(3, "G"))
ht.add(Node(15, "H"))
ht.add(Node(20, "I"))
ht.add(Node(21, "J"))
ht.printHashTable()
print("=========")
ht.remove(120)
ht.remove(15)
ht.printHashTable()
print("==========")
ht.update(20, "K")
ht.printHashTable()