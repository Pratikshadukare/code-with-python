def rev(n):
    rev=0
    dn=n
    rem=0
    while(dn!=0):
        rem=dn%10
        rev=rev*10+rem
        dn//=10
    print("revers number is : ",rev)
    if(rev==n):
        print("number is paindrome ")
    else:
        print("number is not palindrome ")
rev(121)
