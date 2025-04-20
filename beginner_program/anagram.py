
a='aacd'
b='adac'
ca=0
cb=0
for i in a:
    ca+= ord(i)
    
    print(i,":",ord(i))

for i in b:
    cb+= ord(i)

    print(i,":",ord(i))

if len(a)==len(b):
    if cb==ca:
        print("anagram")
    else:
        print("NOT")
print("cb",cb,"ca",ca)