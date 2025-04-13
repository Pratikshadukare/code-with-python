'''
9. **Remove a key from a dictionary**  
   ➤ Input: `{'a': 1, 'b': 2}, key='a'` → Output: `{'b': 2}`
'''

input_dict = {'a': 1, 'b': 2}

def remove_key(d, k):
    new_dict = {}
    for key in d:
        if key != k:
            new_dict[key] = d[key]
    return new_dict

input_dict = {'a': 1, 'b': 2}
print(remove_key(input_dict, 'a'))  
