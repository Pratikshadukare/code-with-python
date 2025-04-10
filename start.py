'''
input =[(do,('cat','dog','dove','duck',''))]
output=['dog','dove']
'''
mylist=[('do',('cat','dog','dove','duck',''))]
op=[]
for i in mylist[0][1]:
    print(i)
    if mylist[0][0]==i[0:len(mylist[0][0])]:
        print('match')
        op.append(i)
        

print(op)
