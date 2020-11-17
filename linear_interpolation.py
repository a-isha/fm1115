import numpy as np
import matplotlib.pyplot as plt

def interpolate(y_t, dt, tim):
    
    #calculate dy_dt from dt*

    dy_dt = (y_t[1] - y_t[0])*(1/dt)
    c = y_t[0] - (dy_dt*t[i]) 
    #print(c)
    
    y_find = (dy_dt*tim) + c
    
    return y_find


def find_i(t_f,t):  # 4.10, section 1 [[uses interpolation function and returns the y value]]
    
    for i in range (0,N):

        if t[i] <= int(t_f) and t[i+1] >= int(t_f+1):
            print('The value of i at which t = {:g} is {:g}'.format(t_f, i))
            #print('The i in function is: ',i)       #test_print
            return i

def find_y(t,Y):       #4.10 sec (b)  
     
    T1 = 1
    dt = 1
    global i
    while  T1>=0 and T1<N:
        T1 = float(input('Enter a T to find y_T:'))
        i = find_i(T1, t)
        y_vals = np.zeros(2)
        y_vals = (Y[i],Y[i+1])
        y_finder = interpolate(y_vals, dt, T1)
        print(y_finder)
        print('End of program')
        
    print('You entered a negative number')    
    return  0

#=======================================================================================================#
N = int(input('Enter max number for "i" - Num:'))

t = np.linspace(0,N-1,N)
y = np.zeros(N)
dt = 1

#taking y-inputs
for ind in range(0,N):
    
    y_in = float(input('Y-value input:'))
    y[ind] = y_in
    
print('Y-array is', y)

print('Initiate functions-')
find_y(t,y)

plt.plot(t,y)
