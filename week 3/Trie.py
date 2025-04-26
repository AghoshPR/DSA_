class TrieNode:
    
    def __init__(self):
        
        self.children = {}
        self.end = False
        
        
class Trie:
    
    def __init__(self):
        
        self.root = TrieNode()
        
    
    def insert(self,word):
        
        node = self.root
        
        for ch in word:
            
            if ch not in node.children:
                node.children[ch] =  TrieNode()
            
            node = node.children[ch]
        
        node.end = True
        
    
    def autocomplete(self,prefix):
        
        node = self.root
        
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        results = []
        
        
    
        def dfs(current_node,path):
            
            if current_node.end:
                results.append(path)
                
            for ch in current_node.children:
                dfs(current_node.children[ch], path+ch)
                
    
        
        
        
        dfs(node,prefix)
        return results
    
    def display(self):
        def dfs(node,level):
            for char,child in node.children.items():
                print(" "*level,f"_{char}")
                dfs(child,level+1)
        dfs(self.root,0)

trie = Trie()
words = ["apple", "app", "apex", "bat", "ball", "ban"]

for w in words:
    trie.insert(w)


    
print(trie.autocomplete('ap'))    



    
    
            
            
            
    
        
        