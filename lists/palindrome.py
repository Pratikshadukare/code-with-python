'''
5. **Check if a list is a palindrome**  
   ➤ Input: `[1, 2, 3, 2, 1]` → Output: `True`

---
'''

input_list = [3,5,1,9,2]

for i in range(1,len(input_list)//2+1):
    if input_list[i-1] == input_list[-i]:
        print("string it=s palindrome")
    else:
        print("string is not palindrome")
        break