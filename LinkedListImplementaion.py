#Implementing linked list DSA in python..

class Node():
    
    #Creating a node...
    #Linked list has two entities which are DATA and POINTER..
    #The DATA has some value and the POINTER contains address of next node..
    #Its like dictonary 
    def __init__(self, item): 
        self.item = item
        self.next = None 

class LinkedList():
    
    def __init__(self):
        self.head = None

if __name__ == 'main':

    linked_list = LinkedList()

    #Assign item values..
    linked_list.head = Node(1)
    second = Node(2)
    Third = Node(3)

    #Connect nodes..
    linked_list.head.next = second
    second.next = third

    #Displaying the linked list..
    while linked_list.head != None:
        print(linked_list.head.item,end = ' ')
        linked_list.head = linked_list.head.next



