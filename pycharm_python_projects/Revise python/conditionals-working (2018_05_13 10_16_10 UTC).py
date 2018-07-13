#!/usr/bin/python3

a, b ,c= 6, 1, 2
print('a ({}) is not less than b ({})'.format(a ,b))    
if a < b:
    print('a ({}) is less than b ({}) c({})'.format(a, b, c))
else:
    print(' {} is not less than  {}'.format(a, b))
    print('a ({}) is not less than b ({})'.format(a ,b))
print("foo" if b > c else "bar")   