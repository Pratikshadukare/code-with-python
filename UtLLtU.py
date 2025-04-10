s1="saHntaNu"

def fun(s1):
    s2=""
    asc=ord(s1[0])
    if(asc>=97 and asc<=122):
        s2=s2+chr(asc-32)
       
    else:
        s2=s2+s1[0]
        

    for ch in s1[1:]:
        print(ord(ch))
        if ord(ch)>=97 and ord(ch)<=122 :
            s2=s2+chr(ord(ch)-32)
            
        else:
             s2=s2+chr(ord(ch)+32)
             
    print(s2)
#fun(s1)
            
def LFuppercase(s):
    s2=""
    l=int(len(s))
    t1=ord(s[0])
    t2=ord(s[-1])
    if t1>=97 and t1<=122:
        t1=chr(ord(t1)-32)
        
    if t2>=97 and t2<=122:
        t2[-1]=chr(ord(t2)+32)
        
    for i in s[1:l-1]:
        s2=s[i]
    ns=t1+s2+t2
    print(ns)

LFuppercase(s1)  
