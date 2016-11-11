from tkinter import *
import time
import random

window = Tk()

canvas = Canvas(window, width=300, height=250, bg="white")
canvas.pack()

#Set x and y velocities
vx = 10.0
vy= 5.0

#Boundaries
x_min = 0
y_min = 0
x_max = 300
y_max = 250

#Create robot representation
id1=canvas.create_rectangle(145,120,155,130)

#Generate x and y coordinates for 500 timesteps
for t in range (1,500):
    x1,y1,x2,y2=canvas.coords(id1)
    #Make robot change direction randomly
    RandomVal=random.randint(1,100)
    if RandomVal>=75:
        vx=-10
        vy=0
    elif RandomVal>=50 and RandomVal<75:
        vx=10
        vy=0
    elif RandomVal>=25 and RandomVal<50:
        vx=0
        vy=10
    else:
        vx=0
        vy=-10
    #If a boundary has been crossed, reverse the direction
    if x1 >= x_max:
        vx = -10.0
    if y1 <= y_min:
        vy = 5.0
    if y2 >= y_max:
        vy = -5.0
    if x1 <= x_min:
        vx = 10.0
    #Reposition the robot
    canvas.coords(id1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    # Pause for 0.5 seconds, then delete the image
    time.sleep(0.1)
window.mainloop
