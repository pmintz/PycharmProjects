#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    #blocks do not determine scope
    z = 112
    #the following are part of the block.  will only print when x < y.
    print('x < y: x is {} and y is {}'.format(x, y))
    print('inside if')
        #causes error because it doesn't belong to any block
        #print('r')
 #causes error because it doesn't belong to any block (minor indentation.  Not fully to left or right)
 #print('\r')
#will always print
print('something else')
#accessing z variable outside of block.  Again, blocks do no determine scope.
print('z is {}'.format(z))

print('\r')
print('**************')
print('\r')

if x > y:
    print('x > y: x is {} and y is {}'.format(x,y))
#can have more than one
elif x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
else:
    print('default')