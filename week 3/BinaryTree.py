class BinaryTree:
    
    def __init__(self,value):
        
        self.value = value
        self.left = None
        self.right = None
        
    
    def insert_left(self,value):
        
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node
            
    
    def insert_right(self,value):
        
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            self.left = self.right
            self.right = new_node
            
    
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
                
    def count(self):
        
        left = self.left.count() if self.left else 0
        right = self.right.count() if self.right else 0
        
        
root = BinaryTree(1)
root.insert_left(2)
root.insert_right(3)
root.left.insert_left(4)
root.left.insert_right(5)
root.right.insert_left(6)
root.right.insert_right(7)
            


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


print("Total Nodes in Binary Tree:", root.count())
        
        
        