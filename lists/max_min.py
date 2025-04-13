'''

1. **Find the maximum and minimum elements in a list**  
   ➤ Input: `[3, 5, 1, 9, 2]` → Output: `Max = 9, Min = 1`

'''

input_list = [3,5,1,9,2]

def min_max_element(li):
    if not list:
        return None,None
    
    else:
        min  = max =li[0]
        for i in range(len(li)):
            
            if li[i]>max:
                max = li[i]
            if li[i] < min:
                min = li[i]
    return min, max

print(min_max_element([2,5,6,7,4,1]))