from tkinter import *
from grid import *
import time
import random
top = Tk()

#Simple canvas with one line to test whether the roomba will pass through walls
grid = grid(500,500,0,[])
for h in range (100,103):
    for w in range (0,75):
        grid.addImpasses([[h,w]])

for w in range (100,103):
    for h in range (0,100):
        grid.addImpasses([[h,w]])

canvas = Canvas(top, height=500,width=500, bg="white")

for i in grid.impasses:
    canvas.create_rectangle(i[1]*1,i[0]*1,(i[1]+1)*1,(i[0]+1)*1, fill="black")

canvas.pack()

###Roomba Movement

#Boundaries
x_min = 0
y_min = 0
x_max = 500
y_max = 500

def detect():
    global move 
    for n in range(0,len(grid.impasses)):
        if n < len(grid.impasses) - 1:
            a1,a2 = grid.impasses[n]
            b1,b2 = grid.impasses[n+1]
            if a1 - b1 == 0:
                if rPositionY >= (a1-5) and rPositionY <= (a1+5) and rPositionX == a2:
                    if rPositionY >= a1:
                        if (rPositionY + vy) <= a1:
                            move = False
                    elif rPositionY <= a1:
                        if (rPositionY + vy) >= a1:
                            move = False
            elif a2 - b2 == 0:
                if rPositionX >= (a2-5) and rPositionX <= (a2+5) and rPositionY == a1:
                    if rPositionX >= a2:
                        if (rPositionX + vx) <= a2:
                            move = False
                    elif rPositionX <= a2:
                        if (rPositionX + vx) >= a2:
                            move = False
 
#Create robot representation
roomba= canvas.create_oval(0,0,10,10, fill="blue")

#Generate x and y coordinates for 500 timesteps
for t in range (1,500):
    move = True
    x1,y1,x2,y2 = canvas.coords(roomba)
    rPositionX = (x1+x2)/2
    rPositionY = (y1+y2)/2
    
    #Make robot change direction randomly
    RandomVal=random.randint(1,100)
    if RandomVal>=75:
        vx=10
        vy=0
    elif RandomVal>=50 and RandomVal<75:
        vx=-10
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
        vy = 10.0
    if y2 >= y_max:
        vy = -10.0
    if x1 <= x_min:
        vx = 10.0

    #Reposition the robot
    detect()

    if move == True:
        canvas.coords(roomba,x1+vx,y1+vy,x2+vx,y2+vy)

    canvas.update()

    #Pause for 0.1 seconds, then delete the image
    time.sleep(0.1)

top.mainloop()

