'''
### 6. First Non-Repeating Character
- **Input:** `"aabbcdd"`  
- **Output:** `"c"`  
- 💡 *Tests logic, string traversal, and dictionary.*

---
'''
input_string = input("enter string you want  :")

out = input_string
d = {}

for i in input_string:
    d[i] = d.get(i,0)+1

for ch in input_string:
    if d[ch] == 1:
        print("First non_repeating charector is" ,ch)
        break
else:
    print("First non_repeating charector is not present in string")
