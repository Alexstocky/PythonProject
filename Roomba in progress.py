class Roomba():
    def __init__(self,grid,gridobj):
        self.index = 0
        #placing the roomba in a random place in the top-left corner of the map and setting it's coordinates
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
        #conditionals for the robot's movement
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
