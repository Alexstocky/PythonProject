import random

class grid:
    def __init__(self,height,width,numDirt,impasses=[]): #Generates a tuple of tuples of dictionaries representing the 'gamespace'. Height is the number of tuples containing dictionaries. Width is the number of dictionaries in each tuple.
        self.grid = []                                   #Impasses is a list of coordinates of place that are inpassable. Spawn right now only only contains the start position of doggo, but will contain roomba at some point. numDirt is the number of dirts to be placed
        for h in range(height):
            self.grid.append([])
            for w in range(width):
                self.grid[h].append({'Impass':False, 'Doggo':False})
            tuple(self.grid[h])
        tuple(self.grid)
        for x in impasses:
             self.grid[x[0]][x[1]] ['Impass'] = True
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
