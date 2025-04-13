'''
9. **Find common elements in two lists**  
   ➤ Input: `[1, 2, 3], [2, 3, 4]` → Output: `[2, 3]`

'''

input_list = [3,5,1,9,2]
input_list2 = [4,5,7,9,2]
common_elem = []

for i in input_list:
    for j in input_list2:
        if i == j :
            common_elem.append(j)

print(common_elem)
        
