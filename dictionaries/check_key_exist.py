'''
3. **Check if a key exists in a dictionary**  
   ➤ Input: `{'x': 10, 'y': 20}, key='y'` → Output: `True`

'''

input_dict = {'x': 10, 'y': 20}
key = 'y'

found = False
for k, v in input_dict.items():
    if key == k:
        found = True
        break

print(found)  # Output: True


