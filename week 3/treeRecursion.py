class BST:

    def __init__(self,key):

        self.key = key
        self.Lchild = None
        self.Rchild = None


    def insert(self,data):

        if self.key is None:
            self.key = data
            return


        if self.key == data:

            return
        
        if self.key > data:

            if self.Lchild:
                self.Lchild.insert(data)
            else:
                self.Lchild = BST(data)
        
        else:

            if self.Rchild:

                self.Rchild.insert(data)
            else:
                self.Rchild = BST(data )

    
    def search(self,data):

        if self.key == data:

            print("Node is found")
            return
        
        if data < self.key:

            if self.Lchild:
                self.Lchild.search(data)
            

            else:

                print("Node is not present in tree! ")
        else:

            if self.Rchild:
                self.Rchild.search(data)
            else:

                print("Node is not present in tree")
    


    def preorder(self):

        print(self.key,end=' ')
        if self.Lchild:
            self.Lchild.preorder()
        if self.Rchild:
            self.Rchild.preorder()
    
    def inorder(self):

        if self.Lchild:
            self.Lchild.inorder()
        print(self.key,end=' ')
        if self.Rchild:
            self.Rchild.inorder()
    
    def postorder(self):

        if self.Lchild:
            self.Lchild.postorder()
        
        if self.Rchild:
            self.Rchild.postorder()
        
        print(self.key,end=' ')

    def level_order(self):
        if self is None:
            return
        queue = [self]
        while queue:
            current = queue.pop(0)
            print(current.key, end=' ')
            if current.Lchild:
                queue.append(current.Lchild)
            if current.Rchild:
                queue.append(current.Rchild)

    
    def min_node(self):
        temp = self

        while temp.Lchild:
            current = current.Lchild
        print("smalest",temp.key)
    
    def max_node(self):
        temp = self

        while temp.Rchild:
            current = current.Rchild
        print("Largest",temp.key)



def count(node):
    if node is None:
        return 0
    return 1+count(node.Lchild)+count(node.Rchild)

# root=BST(10)
# list1=[30,20,2,5,6,7]

# for i in list1:
#     bst.insert(i)  
# print("preorder")
# root.preorder()
# print()

# print("inorder")
# root.inorder()
# print()

# print("postorder")
# root.postorder()
# print()

# print("Level Order:")
# root.level_order()