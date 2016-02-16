import os
import re
import time
import csv
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pylab

#global variables
l=0
n=[0,0,0,0]


fig, ax = plt.subplots()
core1_line, = ax.plot([], [], lw=2)#"lw" stands for line width
core2_line, = ax.plot([], [], lw=3)
core3_line, = ax.plot([], [], lw=5)
ax.grid()
x_time_data, core1_data,core2_data,core3_data = [], [], [],[]#"x_time_data" is time for x coordinate,


#Conversion
def Mhz_To_Ghz(f):
	return f/1000
def Mhz_Or_Ghz(x):
	if ('M' in x):
		x = float(x[:4])
		x =Mhz_To_Ghz(x)
		return x
	else:
		x = float(x[:4])
		return x

#frequency value generation function
def data_gen(t=0):
	while (1):
		time.sleep(1)
		a = os.popen("cpufreq-info | grep \"CPU freq\"").read()	
		m = re.findall('is (.+?)Hz\.\\n', a)
		print m
		j=0
		l=len(m)
		while (j<l):	
			m[j]=Mhz_Or_Ghz(m[j])
			n[j]=m[j]
			j=j+1
        	t+=1
        	yield t

        	
def init():
    ax.set_ylim(-1, 5)
    ax.set_xlim(0, 10)


#update the data
def run(data):
    t= data
    j=0
    x_time_data.append(t)
    j=0
    core1_data.append(n[0])
    core2_data.append(n[1])
    core3_data.append(n[2])
    xmin, xmax = ax.get_xlim()
    if t >= xmax:
        ax.set_xlim(xmax-5,2*xmax)
        ax.figure.canvas.draw()
    core1_line.set_data(x_time_data, core1_data)
    core2_line.set_data(x_time_data, core2_data)
    core3_line.set_data(x_time_data,core3_data)
    return core1_line,core2_line,core3_line


#animation function
ani = animation.FuncAnimation(fig,run,data_gen,blit=False,interval=1000,repeat=False,init_func=init)
plt.show()

