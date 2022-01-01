import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def euler(x0,v0,m=1,G=6.67e-11,M=6.42e23,t_max=10000,dt=1):

    t_array = np.arange(0, t_max, dt)

    pos = np.zeros(shape=(len(t_array),3))
    vel = np.zeros(shape=(len(t_array),3))

    for i in range(len(t_array)):
        if i==0:
            pos[i]=x0
            vel[i]=v0
        else:
            a = -(G*M*pos[i-1])/((np.linalg.norm(pos[i-1]))**3)
            pos[i] = pos[i-1] + dt * vel[i-1]
            vel[i] = vel[i-1] + dt * a
    return [pos,vel,t_array]


def verlet(x0,v0,m=1,G=6.67e-11,M=6.42e23,t_max=10000,dt=1):

    t_array = np.arange(0, t_max, dt)

    pos = np.zeros(shape=(len(t_array),3))
    vel = np.zeros(shape=(len(t_array),3))

    for i in range(len(t_array)):
        if i==0:
            pos[i]=x0
            vel[i]=v0
        elif i==1:
            a = -(G*M*pos[i-1])/((np.linalg.norm(pos[i-1]))**3)
            pos[i] = pos[i-1] + dt * vel[i-1]
            vel[i] = vel[i-1] + dt * a 

        else:
            a = -(G*M*pos[i-1])/((np.linalg.norm(pos[i-1]))**3)
            pos[i] = 2*pos[i-1] - pos[i-2] + (dt**2)*a
            vel[i] = (pos[i]-pos[i-1])/dt

    return [pos,vel,t_array]


def plot(method,name,x0,v0):
    pos,t=method(x0,v0)[0],method(x0,v0)[2]
    x=np.zeros(shape=(len(pos)))
    y=np.zeros(shape=(len(pos)))
    z=np.zeros(shape=(len(pos)))
    for i in range(len(pos)):
        x[i]=pos[i][0]
        y[i]=pos[i][1]
        z[i]=pos[i][2]
    if name=='straight':
        for i in range(len(z)):
            if z[i]<3389500: #radius of mars
                z=z[:i]
                t=t[:i]
                break
        plt.plot(t,z)
        plt.xlabel('Time (s)')
        plt.ylabel('Height')
        plt.title(method.__name__+' height vs time')
        plt.show()
    else:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x,y,z, label=name)
        ax.legend()
        plt.title(method.__name__+' trajectory')
        plt.show()



plot(euler, 'straight',[0,0,5000000],[0,0,0])
plot(euler,'circular',[0,0,5000000],[2926.5,0,0])
plot(euler,'eliptical',[0,0,5000000],[3300,0,0])
plot(euler,'escape',[0,0,5000000],[4000,0,0])

plot(verlet, 'straight',[0,0,5000000],[0,0,0])
plot(verlet,'circular',[0,0,5000000],[2926.5,0,0])
plot(verlet,'eliptical',[0,0,5000000],[3300,0,0])
plot(verlet,'escape',[0,0,5000000],[4000,0,0])