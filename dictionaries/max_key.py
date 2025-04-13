'''
8. **Find the key with the maximum value**  
   ➤ Input: `{'a': 5, 'b': 9, 'c': 2}` → Output: `'b'`

'''

in_dict = {'a': 5, 'b': 9, 'c': 2}
items = list(in_dict.items())
max_key = items[0][0]
max_val = items[0][1]

for k, v in items:
    if v > max_val:
        max_val = v
        max_key = k

print(max_key)  
