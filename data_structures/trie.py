class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,string):
        temp = self.root
        for s in string:
            index = ord(s) - ord('a')
            if not temp.children[index]:
                temp.children[index] = Node()
            temp = temp.children[index]
        temp.end = True
    
    def search(self, string):
        temp = self.root
        for s in string:
            index = ord(s) - ord('a')
            if not temp.children[index]:
                break
            temp = temp.children[index]
        
        return temp.end

if __name__ == '__main__':
    T = Trie()
    T.insert('hello')
    T.insert('world')
    T.insert('blue')
    T.insert('earth')
    T.insert('a')
    T.insert('corrupt')

    print(T.search('money'))
    print(T.search('a'))
    print(T.search('blue'))