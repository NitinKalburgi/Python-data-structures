# Building a stack from scrath
class Stack():

    def __init__(self):
        self.stack = []

    #To push an element in stack
    def push(self,item):
        return self.stack.append(item)

    #To pop an element from stack
    def pop(self):
        if len(self.stack) < 0:
            return None
        return self.stack.pop(-1)

    #To display the stack
    def display(self):
        print(self.stack)

stc = Stack()
stc.push(0)
stc.push(1)
stc.push(2)
stc.push(3)
stc.display()
stc.push(4)
stc.display()
stc.pop()
stc.display()
stc.pop()
stc.display()
