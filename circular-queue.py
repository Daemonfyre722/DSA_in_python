class Queue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=capacity*[None]
        self.front=-1
        self.rear=-1
        self.size=0
    def is_full(self):
        return self.size==self.capacity
    def is_empty(self):
        return self.size==0
    def enqueue(self,item):
        if self.is_full():
            raise Exception('Queue Overflow')
        if self.front==-1:
            self.front=0
        self.rear=(self.rear+1) % self.capacity
        self.queue[self.rear]=item
        self.size+=1
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue Underflow')
        item=self.queue[self.front]
        self.queue[self.front]=None
        self.front=(self.front + 1)%self.capacity
        self.size-=1
        return item
    def front_element(self):
        return self.queue[self.front]
# --- Example Usage ---
print("\n--- Circular Queue Example ---")
cq = Queue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print(f"Front element is: {cq.front_element()}")
print(f"Dequeued: {cq.dequeue()}")
cq.enqueue(40)  # Wraps around
print(f"Front element is now: {cq.front_element()}")
print(f"Queue: {cq.queue}, Front: {cq.front}, Rear: {cq.rear}")
