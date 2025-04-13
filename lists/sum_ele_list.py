'''
3. **Sum all the elements in a list**  
   ➤ Input: `[1, 2, 3, 4]` → Output: `10`

'''

input_list = [1,2,3,4,5,6,7,8]


sum = 0

def sum_list_recursive(lst):
    if not lst:
        return 0  
    return lst[0] + sum_list_recursive(lst[1:])  

print(sum_list_recursive([1, 2, 3, 4])) 

'''
for i in input_list:
    sum+= i
print(sum)
'''