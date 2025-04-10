'''
### 4. Remove Duplicates from a String
- **Input:** `"programming"`  
- **Output:** `"progamin"`  
- 💡 *Tests understanding of set or dict and maintaining order.*

---
'''

input_string = input("enter string you want  :")
remove_duplicate_string = ''
'''
for i in input_string:
    if i not in remove_duplicate_string:
        remove_duplicate_string = remove_duplicate_string + i
print(remove_duplicate_string)
'''
'''
l = []
for i in input_string:
    if i not in l:
        l.append(i)

remove_duplicate_string = "".join(l)
print(remove_duplicate_string)

'''

str_set = set(input_string)
remove_duplicate_string = "".join(str_set)
print(remove_duplicate_string)