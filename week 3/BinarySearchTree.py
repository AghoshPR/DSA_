class BST:
    
    def __init__(self,value):
        
        self.value = value
        self.left = None
        self.right = None
        
    
    
    def insert(self,data):
        
        if self.value is None:
            
            self.value = data
            return
        
        if self.value == data:
            
            return 
        
        if self.value > data:
            
            if self.left:
                
                self.left.insert(data)
            else:
                
                self.left = BST(data)
                
                
        else:
            
            
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
                
                
                
                
                
    def search(self,data):
        
        
        if self.value == data:
            print("Node is found")
            return
        
        if self.value > data:
            
            if self.left:
                self.left.search(data)
            else:
                print("Node is not present in tree")
        
        else:
            
            if self.right:
                self.right.search(data)
            else:
                
                print("Node is not present in the tree")
                
    
    def preorder(self):
        
        print(self.value,end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    
    def inorder(self):
        
        if self.left:
            
            self.left.inorder()
        
        print(self.value,end=' ')
        
        if self.right:
            self.right.inorder()
            
    
    def postorder(self):
        
        
        if self.left:
            
            self.left.postorder()
        
        if self.right:
            self.right.postorder()
            
        print(self.value,end=' ')
        
    
    def levelorder(self):
        
        if self is None:
            return
        
        
        queue = [self]
        
        
        while queue:
            
            temp = queue.pop(0)
            print(temp.value,end=' ')
            
            if temp.left:
                queue.append(temp.left)
                
            if temp.right:
                queue.append(temp.right)
    
    
   
    
    def delete(self,data):
          
        if self is None:
            print("Tree is empty")
            return

        if data < self.value:
            
            if self.left:
                
                self.left = self.left.delete(data)
            
            else:
                
                print("node not found")
                
        elif data > self.value:
            
            if self.right:
                self.right = self.right.delete(data)
            
            else:
                print("node not found")
            
        else:
    
            if self.left is None:
                return self.right
            
            elif self.right is None:
                return self.left
                
            else:
                
                temp = self.right
                while temp.left:
                    temp = temp.left
                self.value = temp.value
                self.right = self.right.delete(temp.value)
     
        return self
    
    def height(self):
        if self is None:

            return -1 
        
        left = self.left.height() if self.left else -1
        right = self.right.height() if self.right else -1

        return 1+max(left,right)
    
    def depth(self,data):

        depth=0
        temp=self

        while temp:
            if data == temp.value:
                return depth
            elif data < temp.value:
                temp = temp.left
            else:
                temp = temp.right
            depth += 1
        return -1
        
    def min_val(self):
        temp = self
        
        while temp.left:
            temp = temp.left
        
        print('min val',temp.value)
        return temp
        
    def max_val(self):
        
        temp=self
        
        while temp.right:
            temp = temp.right
        print('max val',temp.value)
        return temp
    
        
    def count(self):
        
        left_count = self.left.count() if self.left else 0
        right_count = self.right.count() if self.right else 0
        return 1 + left_count + right_count
    
    def kth_smallest(self,k):
        
        self.k = k
        self.result = None
        
        
        def inorder(node):
            
            if not node or self.result is not None:
                return
            
            inorder(node.left)
            self.k -= 1
            if self.k ==0:
                self.result = node.value
                return
            
            inorder(node.right)
            
        inorder(self)
        print(f'{k}th smallest: ',self.result)
        return self.result
        
        
    
    def kth_largest(self,k):
        
        self.k=k
        self.result =None
        
        def inorder(node):
            
            if not node or self.result is not None:
                return
            
            inorder(node.right)
            self.k -=1
            if self.k == 0:
                self.result = node.value
                return
            
            inorder(node.left)
        inorder(self)
        print(f'{k}th largest:',self.result)
        return self.result
        
        

root = BST(50) 

root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)
        
 

print("Preorder Traversal:")
root.preorder()
print("\n")

print("Inorder Traversal:")
root.inorder()  
print("\n")

print("Postorder Traversal:")
root.postorder()  
print("\n")

print("Level Order Traversal:")
root.levelorder()  
print("\n")




root.max_val()

root.delete(70)
root.levelorder()

print("\nTotal Nodes in BST:", root.count())
root.kth_largest(3) 
print('height is',root.height())     
print("Depth :", root.depth(60))   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
    
        