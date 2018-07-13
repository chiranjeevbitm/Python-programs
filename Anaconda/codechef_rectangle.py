# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 19:26:19 2018

@author: Chiranjeev
"""

if __name__ == '__main__':
    t = input()
    for i in range(0, int(t)):
        a = input()
        b = input()
        c = input()
        d = input()

        if(a==b==c==d):
            print ("YES")
        elif(a==b and c==d or a==c and b==d or a==d and c==b):
            print ("YES")
        else:
            print ("NO")


