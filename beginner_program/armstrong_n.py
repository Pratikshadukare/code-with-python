"""
An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
"""

input_num = int(input("Enter Any Number :"))

def find_armstrong(n):
    pow = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        rem = temp % 10
        sum += rem ** pow
        temp //= 10
    
    return sum

if find_armstrong(input_num) == input_num:
    print("number is armstrong number")
else:
    print("number is not  armstrong number")