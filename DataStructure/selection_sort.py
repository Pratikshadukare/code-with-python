def selection_sort(arr):

    for i in range(len(arr)):

        min_index = i

        for j in range(1+i,len(arr)):

            if arr[j] > arr[min_index]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]
        
    return arr

print(selection_sort([3,2,4,5,1,6]))
