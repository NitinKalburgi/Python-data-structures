#Building a Queue from scratch..
class Queue():

    def __init__(self):
        self.queue = []

    #Adding an element in an queue
    def enqueue(self,item):
        return self.queue.append(item)

    #Removing an element from queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    #Displaying the queue
    def display(self):
        print(self.queue)

#Operations testing
que = Queue()
que.enqueue(0)
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.display()
que.dequeue()
que.display()