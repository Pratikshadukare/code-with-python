

def bubble_sort(arr):
     n = len(arr)

     swap = False

     for i in range(n):
          for j in range(n-1):
               if arr[j] > arr [j+1]:
                    arr[j+1] , arr[j] = arr[j] , arr[j+1]
                    swap = True

          if swap is True:
               pass
          else:
               break
     return arr

print(bubble_sort([1,6,5,4,7,8,2,3]))
          
                    