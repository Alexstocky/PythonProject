from tkinter import *
from grid import grid
import time
import random
top = Tk()

#Simple canvas with two lines to test whether the roomba will pass through walls
grid = grid(100,100,0,[])
grid.addImpasses([[50,5],[50,6]])
canvas = Canvas(top, height=500,width=500, bg="white")
line1 = canvas.create_line((100,0),(100,100), width=5)
line2 = canvas.create_line((0,100),(75,100), width=5)

for i in grid.impasses:
    canvas.create_rectangle(i[1]*5,i[0]*5,(i[1]+1)*5,(i[0]+1)*5, fill="black")

wallsDict = {"line1":canvas.coords(line1), "line2":canvas.coords(line2)}

canvas.pack()

###Roomba Movement

#Boundaries
x_min = 0
y_min = 0
x_max = 500
y_max = 500

def detect():
    global move 
    for n in range(1,len(wallsDict)+1):
        a1,b1,a2,b2 = wallsDict["line" + str(n)]
        if a1 - a2 == 0:
            if rPositionX >= (a1 - 10) and rPositionY >= b1 and rPositionY <= b2:
                if (rPositionX + vx) >= a1:
                    move = False
        elif b1 - b2 == 0:
            if rPositionY >= (b1 - 10) and rPositionX >= a1 and rPositionX <= a2:
                if (rPositionY + vy) >= b1:
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

