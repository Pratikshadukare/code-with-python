
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

input_num = int(input("enter the num :"))
print("factorial of number ",input_num, "is ", factorial(input_num))
