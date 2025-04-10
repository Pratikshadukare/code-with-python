class student:
    def __init__(self):
        pass
    stu=[]
    def accepting(self,name,rn,contact):
        self.name=name
        self.rn=rn
        self.contact=contact
        self.stu.append(name)
        self.stu.append(rn)
        self.stu.append(contact)
        
    def disply(self):
        print("name =",self.name)
        print("name =",self.rn)
        print("name =",self.contact)

