# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:09:59 2020

@author: User
"""

import sys
import math as m
import matplotlib.pyplot as plt 

def fixed_point_iteration(f_n, x, eps): 
    counter = 0
    val = f_n(x)
    
    while abs(val - x) > eps and counter < 100:
        val = x
        x = f_n(x)
        
        counter = counter + 1
        
    return x, counter 

       
def Newton_Raph(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - f_value/dfdx(x)
        except ZeroDivisionError:
            print('Error! - derivative zero for x = ', x)
            sys.exit(1)     # Abort with error

        f_value = f(x)
        print(x)
        plt.plot(x, f_value,'*')
        iteration_counter = iteration_counter + 1

    # Here, either a solution is found, or too many iterations

    if abs(f_value) > eps:
        iteration_counter = -1
    
    return x, iteration_counter

if __name__ == '__main__':
    
    
    def f(x):
        return x**3 + 2*x - m.exp(-x)
    
    def f_n(x):
        return  0.5*(m.exp(-x) - x**3)
    
    def dfdx(x):
        return 3*x**2 + 2 + m.exp(-x)
    
    #solution, no_iterations = Newton_Raph(f, dfdx, x=1, eps=1.0e-6)
    solution, no_iterations = fixed_point_iteration(f_n, x=1, eps=1.0e-8)
    
    
    if no_iterations > 0:    # Solution found
        print('Number of function calls: {:d}'.format(1+2*no_iterations))
        print('A solution is: {:f}'.format(solution))
    else:
        print('Solution not found!')
    
