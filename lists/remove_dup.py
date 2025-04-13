''''

4. **Remove duplicates from a list while maintaining order**  
   ➤ Input: `[1, 2, 2, 3, 1]` → Output: `[1, 2, 3]`

'''

input_list = [1,2,2,3,7,8,2]

for i in range(len(input_list)):
    for j in range(len(input_list)-1):
        if input_list[j]> input_list [j+1]:
            input_list[j],input_list[j+1] = input_list[j+1],input_list[j]
print(input_list)
outputlist = []
for i in input_list:
    if i not in outputlist:
        outputlist.append(i)
print(outputlist)