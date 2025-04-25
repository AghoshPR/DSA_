class Node:
    
    def __init__(self,value):
        
        self.value = value
        self.left = None
        self.right = None


class BST:
    
    
    def __init__(self):
        
        self.root = None
        
    
    def insert(self,value):
        
        
        new_node = Node(value)
        
        
        if self.root is None:
            
            self.root = new_node
            return
        
        temp = self.root
        
        while True:
            
            
            if value < temp.value:
                
                if temp.left is None:
                    
                    temp.left = new_node
                    return
                temp = temp.left
                
            else:
                
                
                if temp.right is None:
                    
                    temp.right = new_node
                    return
                temp = temp.right
                
    
    
    def search(self,value):
        
        temp = self.root
        
        while temp is not None:
            
            if value == temp.value:
                return True
            
            elif value < temp.value:
                temp = temp.left
            else:
                
                temp = temp.right
                
        return False
        
                
        
    def find_min(self):
        
        if self.root is None:
            
            return None
        
        temp =self.root
        while temp.left:
            temp=temp.left
        
        return temp.value
        
    
    def find_max(self):
        
        if self.root is None:
            return None
        
        temp= self.root
        
        while temp.right:
            temp=temp.right
            
        return temp.value
        
    
    def count_nodes(self,node):
        
        if node is None:
            
            return 0
        return 1+ self.count_nodes(node.left)+self.count_nodes(node.right)    
        
        

    def levelorder(self):
        if self.root is None:
            return
        
        
        queue=[self.root]
        
        while queue:
            
            current = queue.pop(0)
            print(current.value,end=' ')
            
            
            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
            
    
    
    
    def preorder(self,node):
        
        if node is not None:
            
            print(node.value,end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
            
    
    def inorder(self,node):
        
        if node is not None:
            self.inorder(node.left)
            print(node.value,end=' ')
            self.inorder(node.right)
            
    
    def postorder(self,node):
        
        if node is not None:
            
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value,end=' ')
            
    
    
    
    
    def display(self):
        
        print('preorder',end=' ')
        self.preorder(self.root)
    
    
        print('\ninorder',end= ' ')
        self.inorder(self.root)
        
        
        print('\npostorder',end=' ')
        self.postorder(self.root)
        
        print("levelorder", end=' ')
        bst.levelorder()

bst = BST()
lis=[30,20,10,5,40]

for i in lis:
    bst.insert(i)


print(bst.search(2))
print("min",bst.find_min())
print("max",bst.find_max())
print(bst.count_nodes(bst.root))


bst.display()
    
                

        
        
        
        
        
        
        
        
        
            
            
            
            
            
    
        