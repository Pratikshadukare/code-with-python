
'''
### 2. Check for Palindrome
- **Input:** `"madam"`  
- **Output:** `True`  
- 💡 *Tests ability to compare a string with its reverse.*

'''
input_string = input("enter string you want to revers :")
rev_string = ""

'''
for i in range(1,len(input_string)+1):
    rev_string = rev_string + input_string[-i]
print(rev_string)

if rev_string == input_string:
    print("String is palindrome")
else : 
    string("String is not Palindrome")
'''
flag = True
for i in range(1,len(input_string)//2+1):
    if input_string[i-1] == input_string[-i]:
        pass
    else:
        flag = False
        break


if flag:
    print("String is palindrome")
else : 
    print("String is not Palindrome")