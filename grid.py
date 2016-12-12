import random

'''The data structure which acts as the canvas the roomba moves in, a tuple of tuples (a y-axis) of dictionaries (each cell)'''
class Grid:

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
         self.grid[x[0]][x[1]] ['Dirt'] = False
      self.recoopDirt()
         
   '''Recoops dirt that had walls built on it.'''
   def recoopDirt(self):
      curDirt = 0
      for y in self.grid:
         for x in y:
            if x ['Dirt']:
               curDirt += 1
      curDirt = self.origDirt - curDirt
      print(curDirt)
      i = 0
      for y in range(len(self.grid)):
         for x in range(len(self.grid[y])):
            if random.random() < curDirt/(len(self.grid)*len(self.grid[y])-i) and self.grid[y][x] ['Impass'] == False: 
               curDirt -= 1
               self.grid[y][x] ['Dirt'] = True
               self.dirtlist.append([x,y])
            i += 1

   '''Generates a 'room', with walls surrounding and a record of the dirt within it. Coord is a dictionary, with each corner of the room labelled with it's ordinal direction e.g. 'NW' and is value a tuple containing it's coords. If the coordinate is outside the grid, leave it is false. Entrance is a tuple, with the first value the point along the entrance is on, and the second a letter representing the cardinal direction of the wall it is on e.g. 'S'''
   def genRoom(self,Coord, Entrance):
      Entrance[1] = Entrance[1].upper()
      room = []
      if Coord['NW'][0]:
         self.addImpasses(Grid.genImpasslist(True,Coord['NW'][0],Coord['SW'][1]+1,Coord['NW'][1]))
      if Coord['NW'][1]:  
         self.addImpasses(Grid.genImpasslist(False,Coord['NW'][1],Coord['NE'][0]+1,Coord['NW'][0]))
      if Coord['NE'][0]:
         self.addImpasses(Grid.genImpasslist(True,Coord['NE'][0],Coord['SE'][1]+1,Coord['NE'][1]))
      if Coord['SW'][1]:
         self.addImpasses(Grid.genImpasslist(False,Coord['SW'][1],Coord['SE'][0]+1,Coord['SW'][0]))
      along = {'W':Coord['NW'][0], 'N':Coord['NW'][1], 'E':Coord['NE'][0], 'S':Coord['SW'][1],} [Entrance[1]]
      if Entrance[1] == 'W' or Entrance[1] == 'E':
         room.append([Entrance[0],along])
         self.grid[along][Entrance[0]] ['Impass'] = False
      else:
         room.append([along,Entrance[0]])
         self.grid[Entrance[0]][along] ['Impass'] = False
      for i in Coord:
         i = Coord[i]
         for j in range(0,2):
            if not i[j]:
               i[j] = 0
      for x in range(Coord['NW'][0],Coord['NE'][0]+1):
         for y in range(Coord['NW'][1],Coord['SW'][1]+1):
            if self.grid[y][x] ['Dirt']:
               room.append([x,y])
      self.rooms.append(room)

   '''Makes a list of all entrances in the grid, stores as self.doors. Allows roomba to use as a destination.'''
   def getDoors(self):
      self.doors = []
      for i in self.rooms:
         self.doors.append(i[0])
    
   '''Creates the grid. Height is the number of tuples containing dictionaries. Width is the number of dictionaries in each tuple. Add impasses are as they are in addImpasses. numDirt is the number of dirts to be placed.'''
   def __init__(self,height,width,numDirt,impasses=[]):
        #Contains the actual data structure
        self.grid = []
        #A list of the [x,y] coordinates of cells which are impasses
        self.impasses = []
        #Likewise for dirt
        self.dirtlist = []
        #List of lists describing the contents of a room
        self.rooms = []
        self.height = height
        self.width = width
        self.origDirt = numDirt
        for h in range(height):
            self.grid.append([])
            for w in range(width):
                self.grid[h].append({'Impass':False, 'Doggo':False, 'Roomba':False})
            tuple(self.grid[h])
        tuple(self.grid)
        i = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                #Dirt is set randomly, probability = Amount of dirt to be placed/Number of blocks in which dirt can be placed. 
                if random.random() < numDirt/(len(self.grid)*len(self.grid[y])-i) and self.grid[y][x] ['Impass'] == False: 
                    numDirt -= 1
                    self.grid[y][x] ['Dirt'] = True
                    self.dirtlist.append([x,y])
                else:
                    self.grid[y][x] ['Dirt'] = False
                i += 1
        self.addImpasses(impasses)

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
   def findTarget(self,target):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[x][y] ['DV'] = max(abs(y-target[0]),abs(x-target[1]))
