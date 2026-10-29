import numpy as np
import math
import matplotlib.pyplot as plt

def fun(t,x):
    ##    t = t
    out = math.sin(t * x)

    return out

def RK4(t_0,x_0,T,h):

    N = math.ceil((T-t_0)/h) + 1
    ##    print(N)

    t = np.zeros(N)
    x = np.zeros(N)

    t[0] = t_0

    x[0] = x_0

    for i in range (N - 1):
        t[i+1] = t[i] + h
        k_1 = fun(t[i],x[i])
        k_2 = fun((t[i] + h/2),(x[i] + (h/2)*k_1))
        k_3 = fun((t[i] + h/2),(x[i] + (h/2)*k_2))
        k_4 = fun((t[i] + h),(x[i] + (h)*k_3))
        x[i+1] = x[i] + (h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)

    ##    print(t[100])
    ##    print(x[100])
    return t,x

##RK4(0,1,10,0.1)
##print(math.exp(-2*9.99999999999998))
t,x = RK4(0,4,4,0.01)
##true_x = np.array([math.exp(-10*k) for k in t])
plt.plot(t,x)
##plt.plot(t,true_x)

plt.show()

