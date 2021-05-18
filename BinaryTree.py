#Implementing binary tree in python

#Creating a class node, to create nodes
class Node():

    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

#Inoder transversal
    def inorder(self):
       if self.left:
           self.left.inorder()
       print(str(self.item), end = ' ')
       if self.right:
           self.right.inorder()

#Preorder transversal
    def preorder(self):
        print(str(self.item), end = ' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

#Postorder transversal
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(str(self.item), end = ' ')

#Giving values to nodes
Root = Node(1)
Root.left = Node(2)
Root.right = Node(3)
Root.left.left = Node(4)
Root.left.right = Node(5)
Root.right.right = Node(6)

#Printing inorder trasversal
print("Inorder..: ")
Root.inorder()

#Printing postorder transversal
print("Postorder..: ")
Root.postorder()

#Printing preorder transversal
print("Preorder..: ")
Root.preorder()



