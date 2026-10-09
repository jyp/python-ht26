from graphics import *

N = 20 # number of discs
DISC_SIZE = 30 # size of a disc in pixels
tower_width = (N+1)*DISC_SIZE
tower_height = (N+0.5)*DISC_SIZE


def move(fro,to):
    "Move a disc from fro-stack to to-stack (polymorphic!)"
    to.append(fro.pop())

def hanoi(fro, to, other, n):
    "fro, to, other are stacks"
    if n == 0:
        return
    hanoi(fro, other, to, n-1)
    move(fro,to)
    hanoi(other, to, fro, n-1)

# the graphics rely on:
# invariant (1): a disc not in a tower is placed at the origin of the coordinate system.

class Tower: # we'll make this class respond to stack methods
    def __init__(self, x, y):
        self.discs = []
        self.x = x
        self.y = y
        stake = Rectangle(Point(x-DISC_SIZE/4,y), Point(x+DISC_SIZE/4,y+tower_height) )
        stake.setFill("black")
        stake.draw(win)
    def append(self, disc):
        disc.move(self.x,self.y + DISC_SIZE*len(self.discs)) # use (1)
        update(50)
        self.discs.append(disc)
    def pop(self):
        disc = self.discs.pop()
        disc.move(-self.x,-(self.y + DISC_SIZE*(len(self.discs)))) # maintain (1)
        return disc


win = GraphWin("Hanoi", tower_width*3, round(tower_height+DISC_SIZE), autoflush = False)
win.setCoords(0,0, tower_width*3, tower_height+DISC_SIZE)

# place towers
towers = [Tower(tower_width*(2*n+1)/2,0) for n in [0,1,2]]

# populate 1st tower 
for i in list(reversed(range(N))):
    width = (i+1)*DISC_SIZE
    d = Rectangle(Point(0,0),Point(width,DISC_SIZE))
    d.move(-width/2,0)  # maintain (1) 
    d.draw(win)
    d.setFill("pink")
    towers[0].append(d)

# try:
hanoi(towers[0],towers[2],towers[1],N)
# except:
    # print("Killed")
    
