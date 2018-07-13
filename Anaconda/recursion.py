# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:30:47 2018

@author: Chiranjeev
"""

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
a=[1,2,3]        
recursion(a,0,3,"")  
