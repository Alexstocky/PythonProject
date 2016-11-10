import random

def genGrid(height,width,impasses, spawn, numDirt): #Generates a tuple of tuples of dictionaries representing the 'gamespace'. Height and width are the height and width of the space.
    grid = []                                       #Impasses of a list of coordinates of place that are inpassable. Spawn right now only only contains the start position of doggo,
    for h in range(height):                         #but will contain roomba at some point. numDirt is the number of dirts to be placed
        grid.append([])
        for w in range(width):
            grid[h].append({'Impass':False, 'Doggo':False})
        tuple(grid[h])
    tuple(grid)
    for x in impasses:
         grid[x[0]][x[1]] ['Impass'] = True
    grid[spawn[0]][spawn[1]] ['Doggo'] = True
    i = 0
    for x in grid:
        for y in x:
            if random.random() < numDirt/(len(grid)*len(x)-i) and y ['Impass'] == False: #Dirt is set randomly, probability = Amount of dirt to be placed/Number of blocks in which dirt can be placed. 
                numDirt -= 1                                                             #The equations tends towards an even distibution, but allows variation.
                y ['Dirt'] = True
            else:
                y ['Dirt'] = False
            i += 1
    return grid

def textRepre(grid, wall): # Purely for testing purposes, this produces am ascii representation of the grid at a given time. 'X' for impass, 'D' for dirt, 'G' for Dog, ' ' for empty space and '&' if the dog stands on dirt
    s = ''
    for i in grid:
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

def doggoDirect(grid, dl, time, pd=0, hist=[]): #Engages the doggo's wandering ai for a period of time; dl is the spawn location; pd is the hypothetical 'last move' doggo made, defaults to standing still; time is number of 'turns' function runs for
    def moveDoggo(grid, current, direc): #Edits the values of doggo's x&y to do the actual moving
        grid[current[0]][current[1]] ['Doggo'] = False
        inst = ((0,1,0,0),(0,1,1,0),(1,1,1,0),(1,1,0,0),(1,1,1,1),(0,1,1,1),(1,0,1,1),(1,0,0,0),(1,1,1,0))[direc]
        if inst[1]:
            x = current[0] + inst[0]
        else:
            x = current[0] - inst[0]
        if inst[3]:
            y = current[1] + inst[2]
        else:
            y = current[1] - inst[2]
        x = min(max(x,0),(len(grid)-1))
        y = min(max(y,0),(len(grid[0])-1))
        grid[x][y] ['Doggo'] = True
        return grid, (x,y), direc
    direc = pd
    for i in range(time):
        hist.append(direc)
        grid, dl, pd = moveDoggo(grid, dl, direc)
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
    return grid, dl, direc, hist

#dl = (2,1)
#grid = genGrid(7,7,(),(dl),7)
#print(textRepre(grid, '|'))
#grid, dl, pd, hist = doggoDirect(grid, dl, 10)
#print(textRepre(grid, '|'))

#The above example would if run, generate a 7x7 grid with 7 dirt in it and the dog spawned at 2,1 (which is 3,2 factoring in the 0th value). It would print an ascii representation of this. It would then move the dog for ten 'turns'
#treating the 'previous' move as standing still, and finally return the same grid with the moved dog, as well other pieces of information like the dogs new location, the last move made and a history of the dog's movements.
    
    
    
