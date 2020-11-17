# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:07:48 2020

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

##left to implement the loop on parameter fnction and solve part c

def parameters(prms,T, Y_meas):
    
    press = 1
    
    while (press !=0):
        
        a = float(input('Enter a value for "a" = '))
        prms[0] = a
        b = float(input('Enter a value for "b" = '))
        prms[1] = b
        
        # taking model readings
        for n in range(0,N):
            T[n] = n
            y_model[n] = a*T[n] + b
            
        #calculating sspe
        error_sspe = error_calculation(y_meas, y_model)
        print('The sspe is:', error_sspe)
        
        plt.plot(T, y_model, 'b--', T, y_meas, 'r*')
        plt.show()
        
        press = int(input('Enter 0 to stop, or 1 to continue: '))
        
    return y_model
   

def error_calculation(Y_meas, Y_model):
    
    sum_error = 0
    for n in range(0,len(Y_meas)):
        err = Y_meas[n] - Y_model[n]
        sum_error = err + sum_error
    
    return sum_error*sum_error
        
##------------------------------------------------------------------------------------------------##

N = 5   #number of data
t = np.linspace(0,N-1,N)

y_meas = np.zeros(N)
y_model = np.zeros(N)

#taking measurement y-values
for n in range(0,N):
    
    y_in = float(input('Y-value input:'))
    y_meas[n] = y_in
    
print('Y-measured is', y_meas)

#values of a and b

params = np.zeros(2)
y_model = parameters(params, t, y_meas)



    

