'''
2. **Reverse a list without using built-in reverse functions**  
   ➤ Input: `[1, 2, 3]` → Output: `[3, 2, 1]`

'''
input_list = [3,5,1,9,2] 
new_list = []
for i in range(1,len(input_list)+1):
    new_list.append(input_list[-i])
print(new_list)

'''
def reverse_list(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list = [item] + reversed_list  # Prepend each item
    return reversed_list


print(reverse_list([1, 2, 3])) 

'''