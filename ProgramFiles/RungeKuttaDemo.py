import numpy as np
import math
import matplotlib.pyplot as plt

def fun(t,x):
    ##    t = t
    ##    print(t)
    ##    print(x)
    out = math.sin(t*x)

    return out

def RK4(t_0,x_0,T,h):

    N = math.ceil((T-t_0)/h) + 1
    ##    print(N)

    butcher_tableau = np.array([[0,0,0,0],[1/2,0,0,0],[0,1/2,0,0],[0,0,0,1]])
    q = len(butcher_tableau)
    k = np.zeros(q-1)
    ##    print(k)
    ##    print(k)
    t = np.zeros(N)
    x = np.zeros(N)

    t[0] = t_0

    x[0] = x_0

    ##        k_1 = fun(t[i],x[i])
    ##        k_2 = fun((t[i] + h/2),(x[i] + (h/2)*k_1))
    ##        k_3 = fun((t[i] + h/2),(x[i] + (h/2)*k_2))
    ##        k_4 = fun((t[i] + h),(x[i] + (h)*k_3))

    for i in range (N - 1):
        for j in range (0,q-1):
            t[i+1] = t[i] + h
            ##                print(x[i])
            ##            print(butcher_tableau[j,1:])
            k_value = fun((t[i] + h*butcher_tableau[j,0]),
                          (x[i] + h*np.dot(butcher_tableau[j,1:],k)))
            x[i+1] = x[i] + h*(np.dot(butcher_tableau[(q-1),1:],k))

            k[j] = k_value

    ##    print(t[N-1])
    ##    print(x[N-1])
    return t,x

t,x = RK4(0,4,4,0.01)
##true_x = np.array([math.exp((k**2)/2 - k) for k in t])
plt.plot(t,x)
##plt.plot(t,true_x)

plt.show()

