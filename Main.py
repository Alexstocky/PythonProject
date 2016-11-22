from tkinter import *
import random
# GRID DICTIONARY :
# 0 - Free space
# 1 - Impassable Object eg. wall/table/chair
# 2 - Dirt
class Grid():   #This generates the empty grid #INCLUDES THE WALLS AROUND THE GRID#
    def __init__(self,xSize,ySize):
        self.xSize = xSize
        self.ySize = ySize
    def Generate(self):   
        y = []
        i = 0
        while i in range(self.ySize):
            z=0
            x = []
            while z in range(self.xSize):
                if(z==0 or z==self.xSize-1 or i==0 or i==self.ySize-1):
                    x.append(1)
                    rect = canvas.create_rectangle(z*10, i*10, z*10 + 10, i*10+ 10, fill="black")
                    coords = canvas.coords(rect)
                else:
                    x.append(0)
                z+=1
            y.append(x)
            i+=1
        return y
    def PlaceDirt(self,amount):
        i=0
        while(i<amount):
            randx = random.randint(0,self.xSize-1)
            randy = random.randint(0,self.ySize-1)
            try:
                if(grid1[randx][randy] == 0 and random.random() <((amount-i)/mapsize)):
                    grid1[randx][randy] = 2
                    i+=1
                    canvas.create_rectangle(randx*10, randy*10, randx*10 + 10, randy*10+ 10, fill="brown")
            except IndexError:
                continue
    def PrintGrid(self,grid):
        i=0
        while(i<self.ySize):
            print(grid[i])
            i+=1
##    def PlaceWalls(self,grid):
##        i = 1
##        while i in range(self.ySize):
##            z = 1
##            while z in range(self.xSize):
##                if(z<=self.xSize//2 and i<=self.ySize//2):   # Determine Quadrant to figure out direction wich wall should be face
##                    quadrant = 1                                       # Quadrants :
##                elif(z>self.xSize//2 and i<=self.ySize//2):  #  1  2
##                    quadrant = 2                             #  3  4
##                elif(z<=self.xSize//2 and i>self.ySize//2):
##                    quadrant = 3
##                else:
##                    quadrant = 4
##            if(quadrant=1):
##                it=0
##                maxWallSize = random.random(1,5)
##                direction = random.random(1,2)
##                while(it<maxWallSize):
##                    if(direction==1):
##                        grid[i][z+it]=1
##                    else:
##                        grid 
    def PlaceWalls(self,grid):
        i = 1
        while i in range(self.ySize):
            z = 1
            while z in range(int(self.xSize)):
                    if(grid[i][z] == 0):
                        it = 0
                        maxWallSize = random.randint(1,5)
                        while(it<maxWallSize):
                            try:
                                grid[i][z+it]=1
                                canvas.create_rectangle((z+it)*10, i*10, (z+it)*10 + 10, i*10+ 10, fill="black")
                                it+=1
                            except IndexError:
                                break
                        z=z+maxWallSize+1
                    z+=1
            i+=2
    def GetySize(self):
        return self.ySize

class Roomba():
    def __init__(self,grid,gridobj):
        while True:
            roombaCoordx = random.randint(0,gridobj.GetySize()//4)
            roombaCoordy= random.randint(0,gridobj.GetySize()//4)
            if(grid[roombaCoordx][roombaCoordy] == 0):
                canvas.create_oval(roombaCoordx*10,roombaCoordy*10,roombaCoordx*10 + 12,roombaCoordy*10 + 12,fill="blue")
                grid[roombaCoordx][roombaCoordy] = 'R'
                self.rX = roombaCoordx
                self.rY = roombaCoordy
                break
    #def ChaseDirt(self):
        
win = Tk().withdraw()
prompt = messagebox.askyesno("hi","Do you want to add dirt manually")
win = Tk()
win_height=400
win_width=400
mapsize = ((win_height*win_width)//100)
win.configure(width=win_width,height=win_height)
canvas = Canvas(win,width=win_width,height=win_height)
canvas.place(x=0,y=0, anchor = NW)
grid = Grid(win_width//10,win_height//10)
grid1 = grid.Generate()
grid.PlaceWalls(grid1)
if(prompt==True):
    print("does not work")
else:
    grid.PlaceDirt(win_height//10)
roomba = Roomba(grid1,grid)
#Gameloop should be here
roomba.ChaseDirt()


Tk.update(win)#Delete this 
grid.PrintGrid(grid1) # also for testing delete
