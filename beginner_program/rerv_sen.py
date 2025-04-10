'''
input
sky is blue
output
blue is sky


'''
str="sky is blue"
print(str)
myl=str.split()
#print(myl)
l=len(myl)
myl=myl[::-1]
#print(myl)
str=" ".join(myl)
print(str)
