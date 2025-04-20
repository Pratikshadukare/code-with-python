input_string = input("enter the string : ")

# is = malyalam = madam
# [3:7] is[3:7:2] is[-1]

is_pal = False
for i in range(1,len(input_string)//2 +1 ): 
    if input_string[-i] == input_string[i - 1] :
        is_pal = True

    else:
        is_pal = False

if is_pal :
    print("print pal")
else:
    print("no pal")



