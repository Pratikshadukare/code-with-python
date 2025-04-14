

def merge_sort(arr):
    if len(arr) <= 1 :
        return arr
    mid = len(arr)//2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr,right_arr)

def merge(left,right):
    result = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        
        else:
            result.append(right[i])
            j +=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([2,1,3,4,5,]))