from grid import grid

class Roomba:

    def __init__(self, grid, rl=(0,0)):
        self.rl = rl
        self.grid = grid
        self.direclist = []
        grid.grid[rl[0]][rl[1]] ['Roomba'] = True

    def move(self, inst): #Edits the values of roomba's x&y to do the actual moving
        x = min(max(self.rl[0]+inst[0],0),(len(self.grid.grid)-1))
        y = min(max(self.rl[1]+inst[1],0),(len(self.grid.grid[0])-1))
        if not self.grid.grid[x][y] ['Impass'] == True:
            self.grid.grid[self.rl[0]][self.rl[1]] ['Roomba'] = False
            self.grid.grid[x][y] ['Roomba'] = True
            self.rl = (x,y)

    def findPath(self):
        lowest = float('inf')
        for y in range(-1,2):
            for x in range(-1,2):
                if lowest > self.grid.grid[self.rl[0]+y][self.rl[1]+x] ['DV']:
                    lowest = self.grid.grid[self.rl[0]+y][self.rl[1]+x] ['DV']
                    dirraw = (y,x)
        return dirraw
