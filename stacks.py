class Stack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack=[None]*capacity
        self.top=-1
    
    def is_full(self):
        return self.top+1==self.capacity
    
    def is_null(self):
        return self.top==-1
    
    def push(self,item):
        if self.is_full():
            raise Exception("Stack Overflow")
        self.top+=1
        self.stack[self.top]=item
        

    def pop(self):
        if self.is_null():
            raise Exception('Stack Underflow')
        item=self.stack[self.top]
        self.stack[self.top]=None
        self.top-=1
        return item
    
    def peek(self):
        if self.is_null():
            raise Exception('Stack Underflow')
        return self.stack[self.top]
    
    def size(self):
        return self.top+1