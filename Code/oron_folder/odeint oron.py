
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import tclab
#exercise_1

# define a func
# def model(y,t):
#     k=0.3
#     dydt = -k * y
#     return dydt
#
# # initial condition
# y0 = 1
#
# # values of time
# t= np.linspace(0,20)
#
# # solving ODE
# y = odeint(model, y0 ,t)
#
# # plot results
# plt.plot(t,y)
# plt.xlabel('Time')
# plt.ylabel('Y')
# plt.show()

#exercise_2

# def model(y,t):
#     dydt = -y +1
#     return dydt
#
# y0=0
#
# t=np.linspace(0,5)
#
# y= odeint(model,y0,t)
#
# plt.plot(t,y)
# plt.xlabel('time')
# plt.ylabel('y(t)')
# plt.show()

#exercise_3
#
# def model(y,t):
#     if t<10:
#         u=
#     else:
#         dydt = (-y +u)/5
#
#     return dydt
#
# y0=1
#
# t=np.linspace(0,40,1000)
#
# y= odeint(model,y0,t)
#
# plt.plot(t,y,'r-',label = 'Output y(t)')
# plt.xlabel('time')
# plt.ylabel('y(t)')
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import tclab
import time

n = 300  # Number of second time points (5 min)
tm = np.linspace(0,n,n+1) # Time values

# data
lab = tclab.TCLab()
T1 = [lab.T1]
lab.Q1(50)
for i in range(n):
    time.sleep(1)
    print(lab.T1)
    T1.append(lab.T1)
lab.close()

# simulation
def labsim(TC,t):
    dTCdt = ((23-TC) + 0.8*50)/120.0
    return dTCdt
Tsim = odeint(labsim,23,tm)

# Plot results
plt.figure(1)
plt.plot(tm,Tsim,'b-',label='Simulated')
plt.plot(tm,T1,'r.',label='Measured')
plt.ylabel('Temperature (degC)')
plt.xlabel('Time (sec)')
plt.legend()
plt.show()