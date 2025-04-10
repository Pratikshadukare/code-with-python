li=[1,23,98,98,678]
op=[]
for n in li:
    n=str(n)
    sum=0
    for d in n:
        sum=sum+int(d)
    op.append(sum)
print(op)
