'''
input
p=['123poja123','456gita098','987sita654']
output
int_=[123123,456098,987654]
str_=["poja","gita","sita"]

'''

p=['123poja123','456gita098','987sita654']
int_=[]
str_=[]
for i in p:
    int_var=''
    str_var=''
    for j in i:
        if j.isdigit():
            int_var=int_var+j
        else:
            str_var=str_var+j
    int_.append(int_var)
    str_.append(str_var)

print(int_)
print(str_)
            
        
