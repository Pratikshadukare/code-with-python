st=[]
def push():
    if len(st)==n:
        print("stack is full")
    else:    
        el=input("enter the element :")
        st.append(el)
        print(st)

def pop():
    if not st:
        print("stack is empty")
    else:
        e=st.pop()
        print("remove element ")
        print(st)

def isfull():
    pass

n=int(input("limit of stck ::"))
    
while True:
    print(" enter which operation you want 1.push 2.pop 3.quit")
    ch=int(input())
    if ch==1:
        push()
    elif ch==2:
        pop()

    elif ch==3:
        break
    else:
        print("correct operation ")
    
