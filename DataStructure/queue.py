class Queue:
    def __init__(self):
        self.queue= []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    
    def size(self):
        return len(self.queue)

    
    def display(self):
        return self.queue


if __name__ == "__main__":
    q = Queue()

    
    try:
        print("Dequeue on empty queue:")
        print(q.dequeue())  
    except Exception as e:
        print(e)

    print("Is Queue Empty? ", q.is_empty())  
    print("Queue Size: ", q.size())  
    
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print("Queue after enqueue operations: ", q.display())

    print("Dequeued: ", q.dequeue()) 
    print("Queue after dequeue: ", q.display())

    print("Front element: ", q.peek()) 
    
    print("Is Queue Empty? ", q.is_empty())  
    print("Queue Size: ", q.size())  

    
    print("Handling large test case")
    for i in range(1000):
        q.enqueue(i)

    print(f"Queue Size after 1000 enqueues: {q.size()}")  

    
    for _ in range(1000):
        q.dequeue()

    print("Queue after handling 1000 dequeues:", q.display())
    print("Queue Size after all dequeues: ", q.size()) 
