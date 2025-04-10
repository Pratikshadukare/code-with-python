
def arm (n):
    num=n
    arm=0
    rem=0
    print("orignal number is : ",n)
    l=len(str(n))
    while(num!=0):
        rem=num%10
        arm+=rem**l
        num//=10
    if(arm==n):
        print(" number is armstrong :",arm)
    else:
        print("not armstrng")
arm(371)
arm(456)
        
        
        
    
