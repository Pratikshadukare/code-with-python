'''
8. **Rotate a list by `k` positions**  
   ➤ Input: `[1, 2, 3, 4, 5], k=2` → Output: `[4, 5, 1, 2, 3]`

'''
def rotate_list(lst, k):
    n = len(lst)
    if n == 0:
        return lst
    
    k = k % n  
    
    for _ in range(k):
        last = lst[-1]

        for i in range(n - 1, 0, -1):
            lst[i] = lst[i - 1]
        lst[0] = last
    
    return lst

input_list = [1, 2, 3, 4, 5]
k = 3
print(rotate_list(input_list, k))  