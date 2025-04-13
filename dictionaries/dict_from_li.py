'''
7. **Create a dictionary from two lists**  
   ➤ Input: `keys = ['a', 'b'], values = [1, 2]` → Output: `{'a': 1, 'b': 2}`
'''
list1 = ['a', 'b']
list2 =  [1, 2]
 
dict = {}

for i in list1:

    for j in list2:
        dict[i] = j

print(dict)


