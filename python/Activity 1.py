import numpy as np
import matplotlib.pyplot as plt

def euler(m=1,k=1,x=0,v=1,t_max=100,dt=0.05):

    t_array = np.arange(0, t_max, dt)

    x_list = []
    v_list = []

    for i in range(len(t_array)):
        x_list.append(x)
        v_list.append(v)

        a = -k * x / m
        x = x + dt * v
        v = v + dt * a

    x_array = np.array(x_list)
    v_array = np.array(v_list)

    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, x_array, label='x (m)')
    plt.plot(t_array, v_array, label='v (m/s)')
    plt.legend()
    plt.title('Euler')
    plt.show()


def verlet(m=1,k=1,x=1,v=1,t_max=100,dt=0.1):

    t_array = np.arange(0, t_max, dt)

    x_list = []
    v_list = []
    for t in range(len(t_array)):
        x_list.append(x)
        v_list.append(v)

        if t != 0:
            a = -k * x / m
            x = 2*x - x_list[-2] + (dt**2)*a
            v = (x-x_list[-1])/dt

    x_array = np.array(x_list)
    v_array = np.array(v_list)

    plt.figure(2)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, x_array, label='x (m)')
    plt.plot(t_array, v_array, label='v (m/s)')
    plt.legend()
    plt.title('Verlet')
    plt.show()

#run the 2 functions
euler()
verlet(x=1,dt=1.7)