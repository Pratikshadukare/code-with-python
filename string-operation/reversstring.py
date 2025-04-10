'''
### 1. Reverse a String
- **Input:** `"hello"`  
- **Output:** `"olleh"` 
 '''
 # 1.  using for loop

input_string = input("enter string you want to revers :")
rev_string = ""

'''
for i in range(1,len(input_string)+1):
    rev_string = rev_string + input_string[-i]
print(rev_string)
'''

#2 using while loop
'''
index = 1
while len(input_string) != len(rev_string):
    rev_string = rev_string + input_string[-index]
    index +=1
print(rev_string)

'''

# using slicing

def rev_str(str):
    rev_string = str[::-1]

    return rev_string

print(rev_str(input_string))
