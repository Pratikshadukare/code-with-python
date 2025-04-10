'''
input
a3b4cs
output
aaabbbbccccc

otp=0
n=0
str1=""
str="a3b4c6"
for i in str:
    if i.isalpha():
        c=i
    
    else:
        n=int(i)
    otp=(c*n)
    str1+=otp
    
    
print(str1)
'''
# write a python pprogram [[1,3],[3,6],[5,8],[8,15]]
# output like = [[1,6],[5,8],8,15]]


str = "pratiksha"
newstr = ""
for i in range(len(str)):
    print(-i)
    if -i == 0:
        last = str[-i]
    else:
        newstr = newstr+(str[-i])
newstr = newstr+ last
print(newstr)

print(str[::-1])



