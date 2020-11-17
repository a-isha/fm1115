# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:52:15 2020

@author: User
"""

import numpy as np

def polyarea(x, y):
    
    # checking that length of x and y are equal, and setting num of vertices from length of array
    if(len(x) == len(y)):
        v = len(x)
        #print(v) test print
    
    #calculation of sums of vertices
    sum1 = 0
    for n in range(0, v):
        
        if (n!= v-1):
            res1 = x[n]*y[n+1]
            
        else:
            res1 = x[n]*y[0]
            
        sum1 = sum1 + res1
      
    #print(sum1)          test print
    
    sum2 = 0
    for k in range(0, v):
        
        if (k != v-1):
            res2 = y[k]*x[k+1]
            
        else:
            res2 = y[k]*x[0]
            
        sum2 = sum2 + res2
        
    #print(sum2)         test print
    
    final_calc = abs(sum1 - sum2)
    
    return final_calc
        
##=================================================================================================##        

X = np.array([5, 0, 9, 7])
Y = np.array([1, 7, 2, 5])

print('Calculation of area of a polygon:\n')
z = polyarea(X, Y)

print('Final calculation is: {:g} \n'.format(z) )

area = 0.5*z  

print('Area is {:g}\n'.format(area))
print('Program ends!')
    
    
    
    
    
    
