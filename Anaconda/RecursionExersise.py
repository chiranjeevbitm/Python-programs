# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:42:04 2018

@author: Chiranjeev
"""
#function 1
def fact(n):
    if(n==0):
        return 1
    else:
        return((n)*fact(n-1))
    
#print(fact(5)) 
        
        
def printdec(n):
    #base case
    if(n==0):
        return
    #calling
    print(n)
    printinc(n-1)
    print(n)
    return
#printdec(5)
   

     
def printinc(n):
    #base case
    if(n==0):
        return
    #calling
    print(n)
    printinc(n-1)
    print(n)
    return
#printinc(5)

def printdecinc(n):
    #base case
    if(n==0):
        return
    #calling
    print(n)
    printinc(n-1)
    print(n)
    return
#printdecinc(5)
    


def recursion(arr,vidx,tar,ans):
    ##base case
    if(vidx==len(arr)):
        if(tar==0):
            print(ans)
        return
    ##call
    recursion(arr,vidx+1,tar-arr[vidx],ans+str(arr[vidx]))
    recursion(arr,vidx+1,tar,ans)
    return
#a=[1,2,3]        
#recursion(a,0,3,"")  




def SimpleExpo(b,n):
    if n==0:
        return 1
    else:
        return b*SimpleExpo(b,n-1)

#print (SimpleExpo(3,3))         
    
#function 3
        
def Hanoi(a,f,t,s):
    if(n==1):
        print('move from'+f+'tn'+t)
    else:
        Hanoi(n-1,f,s,t)
        Hanoi(1,f,t,n)
        Hanoi(n-1,s,t,f)

#function 4 -----PALINDROME CHARACTER
        
        
def IsPalindrome(s):
    s=(str.lower(s))
    left =(0)
    right =(len(s)-1)
    while(left<right):
        if(s[left]!=s[right]):
            return False
        left+=1
        right-=1
        
        
    return True


print(IsPalindrome('GUsrUG'))       
    
        
def tochars(s):
    
    s=(str.lower(s))
    ans=('')
    for c in s:
        if(c in str.lower(s)):
            ans = ans+c
    return ans
        
def ispal(s):
    if(len(s)<=1):
        return True
    else:
        return s[0]==s[-1] and ispal(s[1:-1])
    
def ispalindrom(s):
    return ispal(tochars(s))



#int(ispalindrom('GUTUG'))
    

#fibbonacci number
def fib(x):
    assert type(x)==int and x>=0
    if(x==0 or x==1):
        return 1                    
    else:
        return fib(x-1)+fib(x-2)
    
#print(fib(5))
def fibtest(n):
    for i in range(n+1):
        print('fib of' ,i, '=' ,fib(i))
#fibtest(4) 
        
def power(n,p):
    assert type(p)==int 
    #base case
    if(p==0 or n==1):
        return 1
    #calling
    ans=(power(n,p*0.5))
    if(n%2==0):
        return ans*ans
    else:
        return ans*ans*n
print(power(5,5))