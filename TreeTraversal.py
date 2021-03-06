#Define a class node, to create node
class Node():

    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

#Inorder operation
def inorder(root):
        if root:
            inorder(root.left)
            print(str(root.item) + "->", end = ' ')
            inorder(root.right)

#Preorder operation
def preorder(root):
        if root:
            print(str(root.item) + "->", end = " ")
            preorder(root.left)
            preorder(root.right)

#Postorder operation
def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(str(root.item) + '->', end = ' ')



root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(4)
    

print("Inorder")
inorder(root)
print("Preorder")
preorder(root)
print("Postorder")
postorder(root)
