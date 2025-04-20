input_num = int(input("Enter Any Number :"))

def is_perfect(num):
    sum = 0

    for i in range(1,num):
        if num % i == 0:
            sum = sum+ i

    if num == sum:
        return True
    else:
        return False
    
print(is_perfect(input_num))