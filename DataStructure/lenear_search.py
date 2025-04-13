
def liner_search(arr, key):

    for i in range(len(arr)):
        if arr[i] == key :
            return i
    return -1
        
print("element present at ",liner_search([1,9,8,5,7,6,3],4))

