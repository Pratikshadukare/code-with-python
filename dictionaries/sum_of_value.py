'''
4. **Sum all values in a dictionary**  
   ➤ Input: `{'a': 10, 'b': 20}` → Output: `30`
'''

input_dict = {'x': 10, 'y': 20}
sum = 0

for v in input_dict.values():
    sum = sum + v
print(sum)
