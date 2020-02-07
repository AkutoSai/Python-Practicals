# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 00:25:39 2020

@author: Akuto Sai
"""

# Tuples and it's functions

# Tuple packing
person=('Akuto Sai',21)

# Tuple unpacking
(name, age)=person

print(name)
print(age)

# Tuple Comparison
a=(7,8)
b=(1,6)

if a>b:
    print('a is greater')
else:
    print('b is greater')

# Tuple Slicing
c=(1,2,3,4,5,6,7,8,9)
print(c[1:7])

# Tuple as Dictionary Key
d={('akuto','sai'):666}
print(d[('akuto','sai')])    