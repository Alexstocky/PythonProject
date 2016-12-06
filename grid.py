import random

'''The data structure which acts as the canvas the roomba moves in, a tuple of tuples (a y-axis) of dictionaries (each cell)'''
class grid: 

   '''Sets a list of coordinates along a given line upto a given point to become impasses. Needs only be called within grid__init__ function. horv is a bool where True creates a horizontal line and False a vertical line, along is the x or y coord the line is to be based on. upto and start represent the start and end of the line.'''
    def genImpasslist(horv, along, upto, start=0):
        outlist = []
        if horv:
            for x in range(start,upto):
                outlist.append([along, x])
        else:
            for y in range(start,upto):
                outlist.append([y, along])
        return outlist
        
    '''Allows cells to be changed to walls after __init__. Impasses is a list of lists, with each of the list containing the x,y coordinates of a cell to be an impass'''
    def addImpasses(self, impasses):
        self.impasses += impasses
        for x in impasses:
            if x[0] >= self.height or x[1] >= self.width:
                raise IndexError('Grid reference out of range')
            self.grid[x[0]][x[1]] ['Impass'] = True
    
    '''Creates the grid. Height is the number of tuples containing dictionaries. Width is the number of dictionaries in each tuple. Add impasses are as they are in addImpasses. numDirt is the number of dirts to be placed.'''
    def __init__(self,height,width,numDirt,impasses=[]):
        #Contains the actual data structure
        self.grid = []
        #A list of the [x,y] coordinates of cells which are impasses
        self.impasses = []
        #Likewise for dirt
        self.dirtlist = []
        self.height = height
        self.width = width
        for h in range(height):
            self.grid.append([])
            for w in range(width):
                self.grid[h].append({'Impass':False, 'Doggo':False, 'Roomba':False})
            tuple(self.grid[h])
        tuple(self.grid)
        self.addImpasses(impasses)
        i = 0
        xn = -1
        yn = -1 
        for x in self.grid:
            yn += 1
            xn = 0
            for y in x:
                #Dirt is set randomly, probability = Amount of dirt to be placed/Number of blocks in which dirt can be placed. 
                if random.random() < numDirt/(len(self.grid)*len(x)-i) and y ['Impass'] == False: 
                    numDirt -= 1
                    y ['Dirt'] = True
                    self.dirtlist.append([yn,xn])
                else:
                    xn += 1
                    y ['Dirt'] = False
                i += 1

    '''Purely for testing purposes, this produces am text representation of the grid at a given time. DV determines whether DV or general grid is produced, defaults to general grid. For general grid: 'X' for impass, 'D' for dirt, 'G' for dog, 'R' for roomba, ' ' for empty space and '&' if the dog stands on dirt. DV mode produces the grid with each cell containing it's DV value. The cell containing zero contains the roomba'''
    def __str__(self, DV=False):
        if DV:
                s = ''
            for i in self.grid:
                s += '|'+'-'*(len(i)*2-1)+'|'+'\n'
                for x in i:
                    char = str(x['DV'])
                    s += '|'+char
                s += '|'+'\n'
            return s+'|'+'-'*(len(i)*2-1)+'|'+'\n'
        else:
            s = ''
            for i in self.grid:
                s += '|'+'-'*(len(i)*2-1)+'|'+'\n'
                for x in i:
                    char = ''
                    if x['Impass']:
                        char = 'X'
                    elif x['Dirt']:
                        if x['Doggo']:
                                char = '&'
                        else:
                                char = 'D'
                    elif x['Doggo']:
                        char = 'G'
                    elif x['Roomba']:
                        char = 'R'
                    else:
                        char = ' '
                    s += '|'+char

                s += '|'+'\n'
            return s+'|'+'-'*(len(i)*2-1)+'|'+'\n'

    '''Iterates the grid, finding the number of moves between the roomba and every cell, and assigns it to the cell as 'DV'. Fails if roomba is uncalled'''
    def findDirt(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] ['DV'] = max(abs(y-self.dirtlist[0][0]),abs(x-self.dirtlist[0][1]))
