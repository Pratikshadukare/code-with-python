'''
6. **Find the second largest element in a list**  
   ➤ Input: `[10, 20, 5, 8]` → Output: `10`
'''

input_list = [3,5,1,9,2]

def sec_large(input_list):
    if not input_list:
        return None
    
    max = input_list[0]
    for i in input_list:
        if max < i:
            max = i
    
    sec_max = input_list[0]

    for i in input_list:
        if  max != i:
          if sec_max < i  :            
            sec_max = i
    return sec_max , max

print(sec_large(input_list))