list1 = [9,5,6,3,4,2,7]

def Quick_sort(a,l,u):
    if (l<u):
        j = Partition(a,l,u)
        Quick_sort(a,l,j-1)
        Quick_sort(a,j+1,u)


def Partition(a,l,u):
    pivot= a[l]
    i=l
    j= u+1
    while(i<j):
        while(a[i]<pivot and i<=u):
            while(pivot<a[j]):
                j= j-1
            i =i +1
        if(i<j):
            temp = a[i]
            a[i]=a[j]
            a[j]= temp

    a[l] = a[j]
    a[j] = pivot
    return j
            
print(list1)
      