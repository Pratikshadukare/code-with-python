

input_num = int(input("Enter Any Number :"))

a = 0
b = 1
print(a,b,end=" ")
for i in range(input_num):
    a , b  = b , a + b    
    print(b,end=" ")