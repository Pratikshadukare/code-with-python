#Check the number is prime or not
num=int(input("Enter a number:"))
prime=[]
for i in range(num):
    if i == 0 or i == 1 :
        pass
    if i >1 :
        for j in range(2,i):
            if (i % j ) == 0:
               break
    
        else:
            prime.append(i)
            
        
            
print(prime)
print("Count of prime number is:",len(prime))