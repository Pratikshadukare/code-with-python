
def hollow_py(rows):
     n = rows
     for i in range(rows) :
          
          for j in range( 1 , 2 * n ) :
               
               if j == n - i or j == n + j :
                    
                    print("*")


print(hollow_py(5))