import sys
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
    
    def size(self):
        return len(self.data)
    
    def getItem(self, index):
        return self.data[index]
    
class Queue:
    def __init__(self):
        self.array = DynamicArray()
        self.first = 0
        
    def enqueue(self, value):
        self.array.insertAt(self.array.Length(), value)

    def dequeue(self):
        temp = self.array.getItem(self.first)
        self.array.remove(self.first)
        #self.first = (self.first + 1) % self.array.size()
        return temp
    
    def front(self):
        temp = self.array.getItem(self.first)
        return temp
    
    def Length(self):
        return self.array.Length()
    
    def isEmpty(self):
        if self.array.Length() == 0:
            return True
        else:
            return False
        
    def printQueue(self):
        self.array.printArray()
              

class GraphByAdjList:
    def __init__(self, bDirected):
        self.graph = dict()
        self.directed = bDirected
        
    
    def addEdgeInternal(self, source, destination):
        if source in self.graph.keys():
            self.graph[source].append(destination)
        else:
            self.graph[source] = list()
            self.graph[source].append(destination)
    
    def addEdge(self, source, destination):
        self.addEdgeInternal(source, destination)   
        if self.directed == False:
            self.addEdgeInternal(destination, source)
            
    def printGraph(self):
        for node in self.graph.keys():
            print(node, self.graph[node])
            

class GraphByAdjMatrix:
    def __init__(self, numNodes, bDirected):
        self.graph = []
        for i in range(numNodes):
            self.graph.append([0] *numNodes)
        
        self.directed = bDirected
    
    def addEdge(self, srcIndex, destIndex, weight):
        self.graph[srcIndex][destIndex] = weight
        if self.directed == False:
            self.graph[destIndex][srcIndex] = weight

    def printGraph(self):
        for i in range(len(self.graph)):
            print(i, "->", end = " ")
            for j in range(len(self.graph[i])):
                if self.graph[i][j] == 1:
                    print(j, end =" ")
            print("")  
            
    def BFSTraversal(self, startNodeIndex):
        q = Queue()
        q.enqueue(startNodeIndex)
        visited = [False]*len(self.graph)
        visited[startNodeIndex] = True
        
        while(q.isEmpty() == False):
            curNodeIndex = q.dequeue()
            print(curNodeIndex)
            
            for neighbourIndex in range(len(self.graph[curNodeIndex])):
                if self.graph[curNodeIndex][neighbourIndex] == 1:
                    if visited[neighbourIndex] == False:
                        visited[neighbourIndex] = True
                        q.enqueue(neighbourIndex)

                        
    def DFSTraversal(self, nodeIndex, visited):
        visited[nodeIndex] = True
        print(nodeIndex)
        
        for neighbourIndex in range(len(self.graph[nodeIndex])):
            if self.graph[nodeIndex][neighbourIndex] == 1:
                if visited[neighbourIndex] == False:
                    self.DFSTraversal(neighbourIndex, visited)
        

    def nodeWithMaxNeighbour(self):
        countResult = -1
        resultNodeIndex = -1
        for nodeIndex in range(len(self.graph)):
            count = 0
            for neighbourIndex in range(len(self.graph[nodeIndex])):
                if self.graph[nodeIndex][neighbourIndex] == 1:
                    count += 1
            if count > countResult:
                countResult = count
                resultNodeIndex = nodeIndex
        return resultNodeIndex
     
    def minDistanceNode(self, distance, completed):
        minDist = sys.maxint
        minNode = -1
        for i in range(len(self.graph)):
            if distance[i] < minDist and i not in completed:
                minDist = distance[i]
                minNode = i
        return minNode
    
    def shortestPath(self, srcIndex):
        completed = set()
        distance = [sys.maxint]*len(self.graph)
        distance[srcIndex] = 0
        prevNode = dict()
        prevNode[srcIndex] = srcIndex
        while (len(completed) <  len(self.graph)):
            curNodeIndex = self.minDistanceNode(distance, completed)
            completed.add(curNodeIndex)
            if curNodeIndex != -1:
                for j in range(len(self.graph[curNodeIndex])):
                    if self.graph[curNodeIndex][j] > 0 and j not in completed:
                        if distance[j] > distance[curNodeIndex] + self.graph[curNodeIndex][j]:
                            distance[j] = distance[curNodeIndex] + self.graph[curNodeIndex][j]
                            prevNode[j] = curNodeIndex
            else:
                break
        
        return prevNode, distance  


def printPath(prevNodes, key, srcIndex):
    if key ==  srcIndex:
        return
    else:
        temp = prevNodes[key]
        printPath(prevNodes, temp, srcIndex)
        print(temp, "->", key, ", ", end= " ")
    
'''        
myGraph = GraphByAdjList(False)
myGraph.addEdge('A', 'C')
myGraph.addEdge('A', 'B')
myGraph.addEdge('B', 'D')
myGraph.addEdge('B', 'E')
myGraph.addEdge('C', 'E')
myGraph.addEdge('C', 'F')
myGraph.addEdge('D', 'G')
myGraph.addEdge('E', 'G')
myGraph.addEdge('F', 'G')
myGraph.addEdge('A', 'D')
myGraph.printGraph()
'''
print("\n\nMatrix Representation\n\n")
myGraphMatrix = GraphByAdjMatrix(6, False)
myGraphMatrix.addEdge(0, 1, 1)
myGraphMatrix.addEdge(0, 2, 2)
myGraphMatrix.addEdge(1, 2, 1)
myGraphMatrix.addEdge(1, 3, 3)
myGraphMatrix.addEdge(2, 3, 1)
myGraphMatrix.addEdge(2, 4, 4)
myGraphMatrix.addEdge(3, 4, 1)
myGraphMatrix.addEdge(3, 5, 1)
myGraphMatrix.addEdge(4, 5, 1)
myGraphMatrix.addEdge(0, 3, 4)
myGraphMatrix.printGraph()
'''
print("\n\nBFS Traversal\n\n")
myGraphMatrix.BFSTraversal(6)
print("\n\nDFS Traversal\n\n")
visited = [False] *len(myGraphMatrix.graph)
myGraphMatrix.DFSTraversal(0, visited)
print("\nMax Neighbour\n")
print(myGraphMatrix.nodeWithMaxNeighbour())
'''
print("\n\nShortest Path Cost and previous nodes\n\n")
srcNode = 0
prevNode, distance = myGraphMatrix.shortestPath(srcNode)
print(prevNode, distance)
print("\n\nShortest Paths\n\n")
for node in prevNode.keys():
    if node != srcNode:
        print("Shortest path for node ", node, " from node no ",srcNode, ":: ", end = " ")
        printPath(prevNode, node, srcNode)
        print("\n")
    
    

