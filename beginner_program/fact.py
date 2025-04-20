
input_num = int(input("Enter Any Number :"))

def find_factorial(n):
    f = 1
    if n <= 1:
        return f
    else:
        for i in range(2 , n+1):
            f = f * i
            print(f)
    return f

print("Factoral of :", input_num," : " , find_factorial(input_num))

