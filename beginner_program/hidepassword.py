import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER="1234567890"
symbol="!@#$%^&*()_+{}"
all =lower+upper+NUMBER+symbol
lenth=9
password="".join(random.sample(all,lenth))
print(password)
sp="-"*(len(password)-2)
print(sp)
result=password[0]+sp+password[-1]
print(result)


'''
ps="pratiksha"
sp="-"*(len(ps)-2)
print(sp)
result=ps[0]+sp+ps[-1]
print(result)
'''
