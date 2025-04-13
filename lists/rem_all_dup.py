'''
10. **Remove all occurrences of a specific element**  
   ➤ Input: `[1, 2, 2, 3], remove `2` → Output: `[1, 3]`

---
'''

input_list = [3,5,2,9,2]
remove_e= 2
output_list = []

for i in input_list:
    if i is remove_e:
        input_list.remove(remove_e)
print(input_list)
