class ArrayQueue:
    '''Creating an implementation of Queue with Python Array'''
    def __init__(self):
        '''Using Initializer to make storage for queue elements.'''
        self.queue=[]

    def is_empty(self):
        '''Checking if the queue is empty by checking the number of elements in queue.'''
        return len(self.queue)==0
    
    def enqueue(self,item):
        '''Adding elements into a queue.'''
        self.queue.append(item)
        print(f'enqueued {item}')
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Element cant be removed from Empty queue.')
        self.queue.pop(0)

    def front_element(self):
        if self.is_empty():
            raise Exception('The queue is empty.')
    
    def size(self):
        return len(self.queue)

a=ArrayQueue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(1)
a.enqueue(2)
a.dequeue()
print(a.is_empty())
print(a.size())
print(a.front_element())



