# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 20:54:47 2018

@author: Chiranjeev
"""
l = [17,12,41,28,25]
def mystery(l):
     if len(l) < 2:
       return (l)
     else:
       return (mystery(l[1:]) + [l[0]])