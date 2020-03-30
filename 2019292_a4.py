import random as r
import os
import time 

class Grid:

    def __init__(self,n):
        self.n = n
        self.start = r.choice([(0,r.randint(0,n-1)),(r.randint(0,n-1),0),(n-1,r.randint(0,n-1)),(r.randint(0,n-1),n-1)]) #randomly generating start
        self.goal = r.choice([(0,r.randint(0,n-1)),(r.randint(0,n-1),0),(n-1,r.randint(0,n-1)),(r.randint(0,n-1),n-1)])  #randomly generating goal
        #checking they are not same
        while(self.goal==self.start):
            self.start = r.choice([(0,r.randint(0,n-1)),(r.randint(0,n-1),0),(n-1,r.randint(0,n-1)),(r.randint(0,n-1),n-1)]) 
            self.goal = r.choice([(0,r.randint(0,n-1)),(r.randint(0,n-1),0),(n-1,r.randint(0,n-1)),(r.randint(0,n-1),n-1)])
        self.myObstacles = [Obstacle(r.randrange(n),r.randrange(n)) for x in range(r.randrange(1,n))]  #used list comprehension to randomly generate list of Obstacles
        self.myRewards = [Reward(r.randrange(n),r.randrange(n),r.randint(1,9)) for x in range(r.randrange(1,n))] #used list comprehension to randomly generate list of Rewards

    def rotateAnticlockwise(self,n):
        orginal_Obstacles = self.myObstacles
        orginal_Rewards = self.myRewards

        # implementing logic of rotating anticlockwise
        for i in range(n):  
            self.myObstacles = list(map(lambda o : Obstacle(self.n-1-o.y,o.x), self.myObstacles))
            self.myRewards = list(map(lambda re : Reward(self.n-1-re.y,re.x,re.value), self.myRewards))

        # check if goal coincides with obstacle
        if (self.goal[0],self.goal[1]) in list(map(lambda re : (re.x,re.y),g.myObstacles)):
            print('Grid cannot be rotated, Goal coincides with Obstacle')
            time.sleep(1)
            self.myObstacles = orginal_Obstacles
            self.myRewards = orginal_Rewards

        # check if goal coincides with player
        elif (p.x,p.y) in list(map(lambda re : (re.x,re.y),self.myObstacles)):
            print('Grid cannot be rotated, player coincides with Obstacle')
            time.sleep(1)
            self.myObstacles = orginal_Obstacles
            self.myRewards = orginal_Rewards
        return self

    def rotateClockwise(self,n):
        orginal_Obstacles = self.myObstacles
        orginal_Rewards = self.myRewards

        # implementing logic of rotating clockwise
        for i in range(n):
            self.myObstacles = list(map(lambda o : Obstacle(o.y,self.n-1-o.x), self.myObstacles))
            self.myRewards = list(map(lambda re : Reward(re.y,self.n-1-re.x,re.value), self.myRewards))

         # check if goal coincides with obstacle
        if (self.goal[0],self.goal[1]) in list(map(lambda re : (re.x,re.y),self.myObstacles)):
            print('Grid cannot be rotated, Goal coincides with Obstacle')
            time.sleep(1)
            self.myObstacles = orginal_Obstacles
            self.myRewards = orginal_Rewards

         # check if goal coincides with player
        elif (p.x,p.y) in list(map(lambda re : (re.x,re.y),self.myObstacles)):
            print('Grid cannot be rotated, player coincides with Obstacle')
            time.sleep(1)
            self.myObstacles = orginal_Obstacles
            self.myRewards = orginal_Rewards
        return self

    def showGrid(self):
        print('ENERGY:', p.energy)
        for i in range(self.n):
            for j in range(self.n):
                if (i,j) == self.goal: #check if coordinates are of goal
                    print('*',end=' ')
                elif (i,j) == (p.x,p.y): #check if coordinates are of player
                    print('O',end=' ')
                elif (i,j) in list(map(lambda re : (re.x,re.y),self.myObstacles)): #check if coordinates are of Obstacle
                    print('#',end=' ')
                elif (i,j) in list(map(lambda re : (re.x,re.y),self.myRewards)): #check if coordinates are of Rewards
                    k = list(map(lambda re : (re.x,re.y),self.myRewards)).index((i,j))
                    print(self.myRewards[k].value,end=' ')
                elif (i,j) == self.start: #check if coordinates are of start
                    print('_',end=' ')
                else: 
                    print('.',end =' ')
            print()

class Obstacle:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Reward:
    def __init__(self,x,y,value):
        self.x=x
        self.y=y
        self.value=value

class Player:
    def __init__(self):
        #initialized starting position of player and initial energy
        self.x = g.start[0] 
        self.y = g.start[1]
        self.energy = 2*g.n

    def makeMove(self,s):
        s=s.lower() #converting string into lowercase

        #converting string into a list of commands
        j=0
        l=[]
        for i in range(len(s)):
            if s[i].isdigit() and (i == len(s)-1 or s[i+1].isalpha()):
                l.append(s[j:i+1])
                j=i+1
        # taking only valid commands
        l=list(filter(lambda x : x[0].isalpha() and x[1:].isdigit(),l))

        # executing commands in list one by one
        for i in l:
            seconds = 0.5
            k=int(i[1:])

            # command says to go right
            if i[0]=='r':
                for i in range(k):        #updating x and y of player
                    self.y+=1
                    if self.y==g.n:
                        self.y=0
                    if (self.x,self.y) == g.goal:     #if position of player coincides with goal
                        print('YOU WIN CONGRATS')
                        time.sleep(1)
                        exit()
                    self = self.update_energy()    #updating energy
                    g.showGrid()
                    time.sleep(seconds)
                    os.system('cls||clear')

            # command says to go down
            elif i[0]=='d':
                for i in range(k):         #updating x and y of player
                    self.x+=1
                    if self.x==g.n:
                        self.x=0
                    if (self.x,self.y) == g.goal:       #if position of player coincides with goal
                        print('YOU WIN CONGRATS')
                        time.sleep(1)
                        exit()
                    self = self.update_energy()   #updating energy
                    g.showGrid()
                    time.sleep(seconds)
                    os.system('cls||clear')
        
            # command says to go left
            elif i[0]=='l':
                for i in range(k):           #updating x and y of player
                    self.y-=1
                    if self.y==-1:
                        self.y=g.n-1
                    if (self.x,self.y) == g.goal:    #if position of player coincides with goal
                        print('YOU WIN CONGRATS')
                        time.sleep(1)
                        exit()
                    self = self.update_energy()     #updating energy
                    g.showGrid()
                    time.sleep(seconds)
                    os.system('cls||clear')

            # command says to go up
            elif i[0]=='u':
                for i in range(k):              #updating x and y of player
                    self.x-=1
                    if self.x==-1:
                        self.x=g.n-1
                    if (self.x,self.y) == g.goal:      #if position of player coincides with goal
                        print('YOU WIN CONGRATS')
                        time.sleep(1)
                        exit()
                    self = self.update_energy()      #updating energy
                    g.showGrid()
                    time.sleep(seconds)
                    os.system('cls||clear')

            # command says to rotate anticlockwise
            elif i[0] == 'a':
                org=g.myObstacles
                g.rotateAnticlockwise(k)
                if org!=g.myObstacles:        #update energy if rotation has take place
                    self.energy = (self.energy//3)*k
                if self.energy <= 0:          #Game over when energy becomes less than zero
                    print('GAME OVER, Energy Exhausted')
                    time.sleep(1)
                    exit()
                if (self.x,self.y) == g.goal:   #if position of player coincides with goal
                    print('YOU WIN CONGRATS')
                    time.sleep(1)
                    exit()
                g.showGrid()
                time.sleep(seconds)
                os.system('cls||clear')

            # command says to rotate clockwise
            elif i[0] == 'c':
                org=g.myObstacles
                g.rotateClockwise(k)
                if org!=g.myObstacles:        #update energy if rotation has take place
                    self.energy = (self.energy//3)*k
                if self.energy <= 0:            #Game over when energy becomes less than zero
                    print('GAME OVER, Energy Exhausted')
                    time.sleep(1)
                    exit()
                if (self.x,self.y) == g.goal:     #if position of player coincides with goal
                    print('YOU WIN CONGRATS')
                    time.sleep(1)
                    exit()
                g.showGrid()
                time.sleep(seconds)
                os.system('cls||clear')

            else :
                print('Invalid Move')
        g.showGrid()

    def update_energy(self):
        if (self.x,self.y) in list(map(lambda re : (re.x,re.y),g.myObstacles)):  #check if position of player coincides with one of the obstacles
            self.energy -= 4*g.n

        elif (self.x,self.y) in list(map(lambda re : (re.x,re.y),g.myRewards)):      #check if position of player coincides with one of the rewards
            k = list(map(lambda re : (re.x,re.y),g.myRewards)).index((self.x,self.y))
            self.energy += (g.myRewards[k].value*g.n)
            g.myRewards.remove(g.myRewards[k])

        else:
            self.energy -= 1

        if self.energy <= 0:                     #Game over when energy becomes less than zero
            print('GAME OVER, Energy Exhausted')
            time.sleep(1)
            exit()

        return self

if __name__ == '__main__':
    n=int(input('Enter size of grid:  '))
    assert n>1 , 'Grid should be atleast of size 2'
    g=Grid(n)     
    p=Player()
    g.showGrid()
    while(True):
        i=input('Enter Your Move:  ')
        os.system('cls||clear')
        p.makeMove(i)