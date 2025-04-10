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
        if j == n - i + 1 or j == n + i - 1 or (i == n and j % 2 != 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to the next line

    
