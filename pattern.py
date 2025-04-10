'''
for i in  range(9):
    for j in range(9):
        if i==j or j>i :
            print("*",end="")
        else:
            print("",end="")
    print()

str ="pratiksha"
rev=""
l=len(str)
print(l)
for i in range(8,0,-1):
    rev+=str[i]
print(rev)

'''
def rev(str):
    return str==str[::-1]

print(rev("pratiksha"))
if rev("pratiksha"):
    print("string is palindrome")
else:
    print("string is not palindrome")


def rves(s):
    print(s[::-1])
print(rves("pratiksha"))