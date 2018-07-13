# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:36:10 2018

@author: Chiranjeev
"""

def SimpleExpo(b,n):
    if n==0:
        return 1
    else:
        return b*SimpleExpo(b,n-1)

print (SimpleExpo(3,3))         
    