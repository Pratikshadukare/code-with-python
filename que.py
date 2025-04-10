queue=[]

def enqueue():
    elm=input("enter the element ::")
    queue.append(elm)
    print(elm," insert succesfuly !")

def dequeue():
    if not queue:
        print(" queue are empty ")
    else:
        e=queue.pop(0)
        print("removed element is :",e)
        

def show():
    print(queue)


while True:
    ch=int(input("enter the choise 1: enqueue 2: dequeue 3: show 4: exit"))
    if ch==1:
        enqueue()
    if ch==2:
        dequeue()
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("enter valid choice:")
