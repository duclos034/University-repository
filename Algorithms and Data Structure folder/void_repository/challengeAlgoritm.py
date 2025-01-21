ALPHABET_SIZE = 26
class Node:
    def __init__(self):
        self.children = [[0,0] for i in range(ALPHABET_SIZE)]
        
class TRIE:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        word = word.upper()
        temp = self.root
        for i in range(len(word)):
            ch = word[i]
            
            if temp.children[ord(ch) - ord('A')][0] == 0:
               temp.children[ord(ch) - ord('A')][0] = Node()
            
            if i == len(word) - 1:
                temp.children[ord(ch) - ord('A')][1] = 1
                
            temp = temp.children[ord(ch) - ord('A')][0]
            
    def search(self, word):
        word = word.upper()
        temp = self.root
        bFound = self.root
        for i in range(len(word)):
            ch = word[i]
            index = ord(ch) - ord('A')
            
            print(ch, index, temp.children[index])
            if temp.children[index][0] != 0:
                if i == len(word) - 1:
                    if temp.children[index][1] == 1:
                        bFound = True
            else:
                break
            temp = temp.children[index][0]
        return bFound
    

    def printTRIE(self):
        temp = self.root
        q = []
        q.append(temp.children)
        while(len(q) != 0):
            curChild = q.pop(0)
            for i in range(len(curChild)):
                child = curChild[i]
                
                if child[0] != 0:
                    print(chr(ord('A') + i), end= " ")
                    q.append(child[0].children)
            print("\n")
    
    def autoCompleteInternal(self,node, word, result):
        if node[1] ==1:
            result.append(word)
        if node[0] != 0:
            for i in range(len(node[0].children)):
                child = node[0].children[i]
                if child[0] != 0:
                    character = chr(ord("A") + i)
                    self.autoCompleteInternal(child, word +character, result)

    def autoCompleteFeature(self,word):
        temp = self.root
        result = []
        for i in range(len(word)):
            ch = word[i]
            index = ord(ch) - ord('A')
            if temp.children[index][0] != 0:
                temp = temp.children[index][0]
            else:
                return result
        for i in range(len(temp.children)):
            child = temp.children[i]

            if child[0] != 0:
                character = chr(ord('A') + i)
                self.autoCompleteInternal(child, word + character, result)


        return result

    def spellChecker(self):
        return 0 

tr = TRIE()
tr.insert("Hi")
tr.insert("Hello")
tr.insert("hit")
tr.insert("hite")
tr.insert("hip")
tr.insert("hat")



print(tr.autoCompleteFeature("CO"))