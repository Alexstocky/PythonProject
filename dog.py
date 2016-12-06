import random

'''The obsticle which if it reaches the roomba, ends the game. Represented as a True value in the ['Dog'] key in a cell of the grid.'''
class dog:

    '''Creates the dog. grid is the grid object the dog uses, dl is the dogs starting location.'''
    def __init__(self,grid,dl=(0,0)):
        self.hist = []
        self.dl = dl
        #grid object used is saved in case user did not call grid object 'grid'
        self.grid = grid
        self.grid.grid[dl[0]][dl[1]] ['Doggo'] = True
    
    '''Edits the values of doggo's x&y to do the actual moving. Contrary to the similar function in the roomba class, direc is the index of the tuple listed below, which contains the values to add to the current x and y values.'''
    def move(self, direc):
            inst = ((0,0),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))[direc]
            x = min(max(self.dl[0]+inst[0],0),(len(self.grid.grid)-1))
            y = min(max(self.dl[1]+inst[1],0),(len(self.grid.grid[0])-1))
            if not self.grid.grid[x][y] ['Impass'] == True:
                self.grid.grid[self.dl[0]][self.dl[1]] ['Doggo'] = False
                self.grid.grid[x][y] ['Doggo'] = True
                self.dl = (x,y)
            return direc
        
    '''Causes the dog to wander randomly. pd is the 'last move' doggo made which is involved in deciding the next move, defaults to standing still. time is number of 'turns' function runs for.'''
    def engage(self, time, pd=0):
        direc = pd
        for i in range(time):
            self.hist.append(direc)
            pd = self.move(direc)
            #The rest of this function decides the nect move. The probability of any given action is 0.2 for stopping or staying still and 0.1 for every cardinal or ordinal direction, plus 0.1 added to the last direction moved. In this way, the dog tends slightly towards moving the same way in chunks before changing direction, rather than iratic  changes.
            probtab = [0,2]+list(range(3,10))
            for n in range(len(probtab)):
                if probtab[n] >= pd:
                    probtab[n] += 0.5
                probtab[n] /= 10
            probtab.append(1.0)
            rand = random.random()
            for n in range(len(probtab)):
                bn = n + 1
                if rand > probtab[n] and rand < probtab[bn]:
                    direc = n
                    break
        return direc
