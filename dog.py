import random

class dog:

    def __init__(self,gridRef,dl=(0,0)): #Set important values for the object, including linking it to the grid object, which /must/ be called prior to calling this one
        self.hist = []
        self.dl = dl
        self.grid = gridRef
        self.grid.grid[dl[0]][dl[1]] ['Doggo'] = True

    def move(self, direc): #Edits the values of doggo's x&y to do the actual moving
            inst = ((0,0),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))[direc]
            x = min(max(self.dl[0]+inst[0],0),(len(self.grid.grid)-1))
            y = min(max(self.dl[1]+inst[1],0),(len(self.grid.grid[0])-1))
            if not self.grid.grid[x][y] ['Impass'] == True:
                self.grid.grid[self.dl[0]][self.dl[1]] ['Doggo'] = False
                self.grid.grid[x][y] ['Doggo'] = True
                self.dl = (x,y)
            return direc
    
    def engage(self, time, pd=0): #Engages the doggo's wandering ai for a period of time; dl is the spawn location; pd is the hypothetical 'last move' doggo made, defaults to standing still; time is number of 'turns' function runs for
        direc = pd
        for i in range(time):
            self.hist.append(direc)
            pd = self.move(direc)
            probtab = [0,2]+list(range(3,10)) #Everything in this function south of here does the math surrounding the random assignment of the next direction. In essences, the probability of any given action is 0.2 for stopping or staying
            for n in range(len(probtab)):     #still and 0.1 for every direction, plus 0.1 added to the last direction moved. In this way, the dog tends slightly towards moving the same way in chunks before changing direction, rather than 
                if probtab[n] >= pd:          #iratic  changes. In the final implimentation, it would be good if the doggo also had a slight tendency towards the robot, so that it is drifting that way, but how you would do this considering
                    probtab[n] += 0.5         #walls and the like, I have not considered.
                probtab[n] /= 10
            probtab.append(1.0)
            rand = random.random()
            for n in range(len(probtab)):
                bn = n + 1
                if rand > probtab[n] and rand < probtab[bn]:
                    direc = n
                    break
        return direc
