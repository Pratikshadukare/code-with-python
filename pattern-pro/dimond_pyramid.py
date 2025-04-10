'''
    *
   * *
  * * *
 * * * *
  * * *
   * *
    *
'''

n = int(input("enter the no "))
for i in range(n):
    print(" "*(n-i)+" *"*(i))

for i in range(n):
    print(" "*i+" *"*(n-i))