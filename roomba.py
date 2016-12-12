from grid import grid

'''Moves within the grid and collects dirt, avoiding the dog. Represented as a True value in the ['Roomba'] key in the grid.'''
class Roomba:
    
    '''Creates the roomba. grid is the grid object roomba uses. rl is the starting location.'''
    def __init__(self, grid, rl=(0,0)):
        self.rl = rl
        #The grid object is saved in case the user does not call the grid object 'grid'
        self.grid = grid
        #Likewise for grid
        grid.roomba = self
        grid.grid[rl[0]][rl[1]] ['Roomba'] = True
        self.destlist = []
        for i in self.grid.rooms:
            self.destlist += i + [i[0]]
        dirtlist = [i for i in self.grid.dirtlist for j in self.grid.rooms if i not in j]
        self.destlist += dirtlist
                    

    '''Edits the values of roomba's x&y to do the actual moving. inst is a tuple containing values to added to the x or y values, these can be 1,0 or -1. findPath returns a compatable input.'''
    def move(self, inst):
        x = min(max(self.rl[0]+inst[0],0),(len(self.grid.grid)-1))
        y = min(max(self.rl[1]+inst[1],0),(len(self.grid.grid[0])-1))
        if not self.grid.grid[x][y] ['Impass'] == True:
            self.grid.grid[self.rl[0]][self.rl[1]] ['Roomba'] = False
            self.grid.grid[x][y] ['Roomba'] = True
            self.rl = (x,y)
        #Pass that there is an impass, and set of instructions to deal with this.

    '''Finds the direction to the nearest dirt and returns the changes to x and y needed as a tuple.'''
    def findPath(self):
        lowest = float('inf')
        for y in range(-1,2):
            for x in range(-1,2):
                if lowest > self.grid.grid[self.rl[0]+y][self.rl[1]+x] ['DV']:
                    lowest = self.grid.grid[self.rl[0]+y][self.rl[1]+x] ['DV']
                    dirraw = (y,x)
        return dirraw
