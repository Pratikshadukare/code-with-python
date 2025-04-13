'''
2. **Merge two dictionaries**  
   ➤ Input: `{'a': 1}, {'b': 2}` → Output: `{'a': 1, 'b': 2}`


'''
dict1 = {'a': 1}
dict2 ={'b': 2}

output_dict = dict1

for k,v in dict2.items():
    output_dict[k] = v
print(output_dict)

'''
dict1 = {'a': 1}
dict2 = {'b': 2}

# Create a new dictionary to store the result
output_dict = {}

# Add items from dict1
for k, v in dict1.items():
    output_dict[k] = v

# Add items from dict2
for k, v in dict2.items():
    output_dict[k] = v

print(output_dict)  # Output: {'a': 1, 'b': 2}

'''