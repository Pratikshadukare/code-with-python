'''
### 5. Check if Two Strings are Anagrams
- **Input:** `"listen", "silent"`  
- **Output:** `True`  
- 💡 *Tests sorting or dictionary usage to compare characters.*

'''

input_string1 = input("enter string you want  :")
input_string2 = input("enter string you want  :")
    
if len(input_string1) == len(input_string2):
    for i in input_string1:
        ascci_count1 += ord(i)
    for i in input_string2:
        ascci_count2 += ord(i)
    if ascci_count1 == ascci_count2:
        print("input String are Anagram")
    else:
         print("input String are not Anagram")
else:
    print("input String are not Anagram")



