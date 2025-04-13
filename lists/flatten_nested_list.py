'''
7. **Flatten a nested list**  
   ➤ Input: `[[1, 2], [3, 4], [5]]` → Output: `[1, 2, 3, 4, 5]`

'''


input_list = [[1, 2], [3, 4], [5]]
output_list = []

for i in input_list:
    if isinstance(i, list):
        for j in i:
            output_list.append(j)
    else:
        output_list.append(i)

print(output_list)  # Output: [1, 2, 3, 4, 5]
