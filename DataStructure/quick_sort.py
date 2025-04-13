

def quick_sort(arr):
    if len(arr) <= 1:
          return arr
    mid = len(arr)//2
    pivote = arr[0]
    left_arr = [ x for x in arr[1:] if x < pivote ]
    right_arr = [ x for x in arr[1:] if x > pivote ]

    return quick_sort(left_arr) +[pivote]+ quick_sort(right_arr)

print(quick_sort([5,6,4,3,7,2,8,1]))


     
    