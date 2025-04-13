'''
1. **Count the frequency of elements in a list using a dictionary**  
   ➤ Input: `[1, 2, 2, 3, 1]` → Output: `{1: 2, 2: 2, 3: 1}`

'''

input_list = [1, 2, 2, 3, 1]

out_dict = {}

for i in input_list:
    out_dict[i] = out_dict.get(i,0)+1

print(out_dict)