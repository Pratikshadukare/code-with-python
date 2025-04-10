
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class llist:
    def __init__(self):
        self.head=None

    def trav(self):
        if self.head is None:
            print("linkedlist is empty ")

        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.ref

    def inbeg(self,data):
        newnode=Node(data)
        newnode.ref=self.head
        self.head=newnode

    def end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode

        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode


    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present ")

        else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode


    def add_before(self,data,x):
        if self.head is None:
            print("linkedlist empty")
            return

        if self.head.data==x:
            newnode=Node(data)
            newnode.ref=self.head
            self.head=newnode
            return

        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("node is not found ")
        else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode

        


obj=llist()
obj.inbeg(50)
obj.end(60)
obj.inbeg(10)

obj.inbeg(40)

obj.trav()
