import random

class grid:

    #Simplifies the process of creating walls by creating lists of coordinates along a given line upto a given point. Needs only be called within grid.__init__ function.
    #horv is a bool where True creates a horizontal line and False a vertical line, along is the x or y coord the line is to be based on. upto and start represent the start and end of the line.
    def genImpasslist(horv, along, upto, start=0):
        outlist = []
        if horv:
            for x in range(start,upto):
                outlist.append([along, x])
        else:
            for y in range(start,upto):
                outlist.append([y, along])
        return outlist
        
    def addImpasses(self, impasses):
        self.impasses += impasses
        for x in impasses:
             self.grid[x[0]][x[1]] ['Impass'] = True
    
    def __init__(self,height,width,numDirt,impasses=[]): #Generates a tuple of tuples of dictionaries representing the 'gamespace'. Height is the number of tuples containing dictionaries. Width is the number of dictionaries in each tuple.
        self.grid = []                                   #Impasses is a list of coordinates of place that are inpassable. Spawn right now only only contains the start position of doggo, but will contain roomba at some point. numDirt is the number of dirts to be placed
        self.impasses = []
        for h in range(height):
            self.grid.append([])
            for w in range(width):
                self.grid[h].append({'Impass':False, 'Doggo':False})
            tuple(self.grid[h])
        tuple(self.grid)
        self.addImpasses(impasses)
        i = 0
        for x in self.grid:
            for y in x:
                if random.random() < numDirt/(len(self.grid)*len(x)-i) and y ['Impass'] == False: #Dirt is set randomly, probability = Amount of dirt to be placed/Number of blocks in which dirt can be placed. 
                    numDirt -= 1                                                             #The equations tends towards an even distibution, but allows variation.
                    y ['Dirt'] = True
                else:
                    y ['Dirt'] = False
                i += 1

    def represent(self, wall='|'): # Purely for testing purposes, this produces am ascii representation of the grid at a given time. 'X' for impass, 'D' for dirt, 'G' for Dog, ' ' for empty space and '&' if the dog stands on dirt
        s = ''
        for i in self.grid:
            s += wall+'-'*(len(i)*2-1)+wall+'\n'
            for x in i:
                char = ''
                if x['Impass']:
                    char = 'X'
                else:
                    if x['Dirt']:
                        if x['Doggo']:
                            char = '&'
                        else:
                            char = 'D'
                    elif x['Doggo']:
                        char = 'G'
                    else:
                        char = ' '
                s += wall+char
            
            s += wall+'\n'
        return s+wall+'-'*(len(i)*2-1)+wall+'\n'
