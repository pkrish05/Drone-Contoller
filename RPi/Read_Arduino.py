# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:45:06 2020

@author: Patel
"""

from Arduino_Serial import Arduino_Serial
import time
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# Arduino Connection Part
ard = Arduino_Serial('COM4', 115200)
ard.connect()
time.sleep(2)

def getvalue(ard):
    conn = ard.connection()
    YPR = {'Yaw' : [], 'Pitch' : [], 'Roll' : []}
    try:
        for i in range(0):
            print(str(conn.readline().decode()))
        print('Hi')
        while True:
           data = str(conn.readline().decode())
           data = data[:-2]
           data_list = data.split(" ")
           if len(YPR['Yaw']) > 1:
               return YPR
           YPR['Yaw'].append(data_list[0].split(":")[1])
           YPR['Pitch'].append(data_list[1].split(":")[1])
           YPR['Roll'].append(data_list[2].split(":")[1])
           #print(YPR)
    except:
        print('Bye...')
        #ard.deconnect()
        #raise Exception("Error Printing")


# Plotting values

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x1 = []
y1 = []
y2 = []
y3 = []


def animate(i, x1, y1, y2, y3):

    # Read MPU6050 Roll Value
    YPR = getvalue(ard)
    if (YPR != None):
        isfloat = True
        try:
            float(YPR['Roll'][0])
            float(YPR['Pitch'][0])
            float(YPR['Yaw'][0])
        except ValueError:
            isfloat = False
        if isfloat:
            roll = float(YPR['Roll'][0])
            pitch = float(YPR['Pitch'][0])
            yaw = float(YPR['Yaw'][0])
            print(roll)

            # Add x and y to lists
            x1.append(len(y1))
            y1.append(roll)
            y2.append(pitch)
            y3.append(yaw)

            # Limit x and y lists to 20 items
            x1 = x1[-25:]
            y1 = y1[-25:]
            y2 = y2[-25:]
            y3 = y3[-25:]

            # Draw x and y lists
            ax.clear()
            ax.plot(x1, y1, color='red')
            ax.plot(x1, y2, color='blue')
            ax.plot(x1, y3, color='green')
            red_patch = mpatches.Patch(color='red', label='Roll')
            blue_patch = mpatches.Patch(color='blue', label='Pitch')
            green_patch = mpatches.Patch(color='green', label='Yaw')
            ax.legend(handles=[red_patch, blue_patch, green_patch])
            plt.title('Roll Pitch Yaw - Angles')
    
anim = animation.FuncAnimation(fig, animate, fargs=(x1, y1, y2, y3), interval=1, frames=150)
plt.show()
print('Bye...')
ard.deconnect()
