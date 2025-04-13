'''
    *
   * *
  *   *
 *     *
* * * * *
'''

n = 5  # Number of rows

for i in range(1, n+1):
    for j in range(1, 2*n):  # Iterate over columns
        if j == n - i + 1 or j == n + i - 1 :
            print("*", end="")
        else:
            print(" ", end="")
    print() 

for i in range(1,n+1):
    for j in range(i):
        print(" ", end = "")
    for j in range(2*(n-i)-1):
        if j == 0 or j == 2*(n - i) - 2 or i == 0:
            print("*",end = "")
        else :
            print(" ",end = "")
        
    print()
