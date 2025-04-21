class Node:
    
    def __init__(self,value):
        
        self.value = value
        self.left=None
        self.right=None


class BST:
    
    def  __init__(self):
        self.root = None
         
    def insert(self,value):
        
        new_node=Node(value)
        
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
                    
                    temp.right=new_node
                    return
                temp = temp.right
                
    
    def inorder(self,node):
         
        if node is not None:
            
            self.inorder(node.left)
            print(node.value,end=' ')
            self.inorder(node.right)
            
    
    def preorder(self,node):
        
        if node is not None:
            
            print(node.value,end=' ')              
            self.preorder(node.left)
            self.preorder(node.right)


            #     100,400,300,200
                

#     100
#         \
#         400
#        /
#      300
#     /
#   200
            
    def postorder(self,node):
        
        if node is not None:
            
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value,end=' ')
            
            
    def display(self):
        
        print("Inorder",end=' ')
        self.inorder(self.root)
        
        print("preorder",end=' ')
        self.preorder(self.root)
        
        
        print("postorder",end=' ')
        self.postorder(self.root)
        
        print()
        
bst=BST()

bst.inser(10)
bst.inser(20)
bst.inser(5)

bst.display()




# list1=[30,20,2,5,6,7]

# for i in list1:
#     bst.insert(i)

            