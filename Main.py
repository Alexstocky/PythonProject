from tkinter import *
import random
import time
# GRID DICTIONARY :
# WHEN USING GRID[][] FIRST ONE IS Y YOU S!%@#
# 0 - Free space
# 1 - Impassable Object eg. wall/table/chair
# 2 - Dirt
class Grid():   #This generates the empty grid #INCLUDES THE WALLS AROUND THE GRID#
    def __init__(self,xSize,ySize):
        self.xSize = xSize
        self.ySize = ySize
    def testout(self,x,y):
        grid1[x][y]=4
        self.PrintGrid(grid1)
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
        self.dirtx = []
        self.dirty = []
        while(i<amount):
            randx = random.randint(0,self.xSize)
            randy = random.randint(0,self.ySize)
            try:
                if(grid1[randy][randx] == 0 and random.random() <((amount-i)/mapsize)):
                    grid1[randy][randx] = 2
                    self.dirtx.append(randx)
                    self.dirty.append(randy)
                    i+=1
                    canvas.create_rectangle(randx*10, randy*10, randx*10 + 10, randy*10+ 10, fill="red")
            except IndexError:
                continue
    def PrintGrid(self,grid):
        i=0
        while(i<self.ySize):
            print(grid[i])
            i+=1
            
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
    def GetxSize(self):
        return self.xSize

class Roomba():
    def __init__(self,grid,gridobj):
        self.index = 0
        while True:
            roombaCoordx = random.randint(0,gridobj.GetxSize()//4)
            roombaCoordy= random.randint(0,gridobj.GetySize()//4)
            if(grid[roombaCoordy][roombaCoordx] == 0):
                self.roomba = canvas.create_rectangle(roombaCoordx*10 , roombaCoordy*10,roombaCoordx*10 + 10,roombaCoordy*10 + 10,fill="green")
                grid[roombaCoordy][roombaCoordx] = 'R'
                self.rx = roombaCoordx
                self.ry = roombaCoordy
                break
    def ChaseDirt(self,grid,gridobj):
        time.sleep(0.01)
        canvas.delete(self.roomba)
        print("ry",self.ry,"rx",self.rx,"DIRTY",gridobj.dirty[self.index],"DIRTX",gridobj.dirtx[self.index], " INDEX " , self.index)
        if(self.ry < gridobj.dirty[self.index] and self.rx < gridobj.dirtx[self.index]):
            grid[self.ry][self.rx]=0
            self.ry+=1
            self.rx+=1
        elif(self.ry < gridobj.dirty[self.index] and self.rx > gridobj.dirtx[self.index]):
            grid[self.ry][self.rx]=0
            self.ry+=1
            self.rx-=1
        elif(self.ry > gridobj.dirty[self.index] and self.rx < gridobj.dirtx[self.index]):
            grid[self.ry][self.rx]=0
            self.ry-=1
            self.rx+=1
        elif(self.ry > gridobj.dirty[self.index] and self.rx > gridobj.dirtx[self.index]):
            grid[self.ry][self.rx]=0
            self.ry-=1
            self.rx-=1
        elif(self.ry == gridobj.dirty[self.index] and self.rx < gridobj.dirtx[self.index]):
            grid[self.ry][self.rx]=0
            self.rx+=1
        elif(self.ry == gridobj.dirty[self.index] and self.rx > gridobj.dirtx[self.index]):
            grid[self.ry][self.rx]=0
            self.rx-=1
        elif(self.ry < gridobj.dirty[self.index] and self.rx == gridobj.dirtx[self.index]):
            grid[self.ry][self.rx]=0
            self.ry+=1
        elif(self.ry > gridobj.dirty[self.index] and self.rx == gridobj.dirtx[self.index]):
            grid[self.ry][self.rx]=0
            self.ry-=1
        else:
            self.index+=1
            self.roomba = canvas.create_rectangle(self.rx*10 , self.ry*10,self.rx*10 + 10,self.ry*10 + 10,fill="white")
        grid[self.ry][self.rx]="R"
        self.roomba = canvas.create_rectangle(self.rx*10 , self.ry*10,self.rx*10 + 10,self.ry*10 + 10,fill="blue")
win = Tk().withdraw()
prompt = messagebox.askyesno("hi","Do you want to add dirt manually")
win = Tk()
win_height=100
win_width=100
mapsize = ((win_height*win_width)//100)
win.configure(width=win_width,height=win_height)
canvas = Canvas(win,width=win_width,height=win_height)
canvas.place(x=0,y=0, anchor = NW)
grid = Grid(win_width//10,win_height//10)
grid1 = grid.Generate()
grid.PlaceWalls(grid1)
if(prompt==True):
    print("does not work yet")
else:
    grid.PlaceDirt(win_height//10)
roomba = Roomba(grid1,grid)
#Gameloop should be here
while True:
    roomba.ChaseDirt(grid1,grid)
    Tk.update(win)
    grid.PrintGrid(grid1)
#Gameloop end
