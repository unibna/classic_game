from config import *
from random import choice

PACMAN_DIR = os.path.join(IMAGE_DIR,"Pacman")
GHOST_DIR = os.path.join(IMAGE_DIR,"Ghost")

class character:
    
    img = None
    images = {}
    heading = (0,1)


    def __init__(self, window, row=None, col=None):
        self.window = window
        self.row = row
        self.col = col

        self.loadImages()
        self.config()

    def getPos(self):
        return (self.row, self.col)

    def config(self):
        pass
    
    def loadImages(self):
        pass

    def draw(self):
        pass

    def canMove(self):
        row_t = self.row + self.heading[0]
        col_t = self.col + self.heading[1]

        try:
            if maze[row_t][col_t] != 1:
                return True
            return False
        except:
            print('[Error] Out of range')
            return False

    def move(self):
        if self.canMove():
            self.row += self.heading[0]
            self.col += self.heading[1]

    def moveRight(self):
        self.heading = (0,1)

    def moveLeft(self):
        self.heading = (0,-1)

    def moveUp(self):
        self.heading = (-1,0)

    def moveDown(self):
        self.heading = (1,0)

class Pacman(character):

    cur_index = 0

    def config(self):
        self.img = self.images[self.cur_index]
        
    def loadImages(self):
        self.images = [
            pygame.image.load(os.path.join(PACMAN_DIR, 'pacman_1.png')),
            pygame.image.load(os.path.join(PACMAN_DIR, 'pacman_2.png')),
            pygame.image.load(os.path.join(PACMAN_DIR, 'pacman_3.png')),
        ]

    def draw(self):
        pos = (self.col*30, self.row*30)

        self.cur_index += 1
        if self.cur_index == 3:
            self.cur_index = 0
        
        # Get image
        self.img = self.images[self.cur_index]
        # Tranform
        if self.heading == (0,1):
            pass
        elif self.heading == (0,-1):
            self.img = pygame.transform.flip(self.img,True,False)
        elif self.heading == (1,0):
            self.img = pygame.transform.rotate(self.img, -90)
        elif self.heading == (-1,0):
            self.img = pygame.transform.rotate(self.img, 90)

        self.window.blit(self.img, pos)

    def eat(self):
        if maze[self.row][self.col] == 2:
            maze[self.row][self.col] = 0
            return True
        return False

class Ghost(character):

    # images = {
    #     'ghost_1': pygame.image.load(os.path.join(GHOST_DIR, 'ghost_1.png')),
    # }

    def __init__(self,window,row=None,col=None):
        super().__init__(window,row,col)
        self.loadImages()
        self.img = self.images['ghost_1']
        self.heading = self.getRandomHeading()

    def loadImages(self):
        self.images = {
            'ghost_1': pygame.image.load(os.path.join(GHOST_DIR, 'ghost_1.png')),
        }
    def getRandomHeading(self):
        heading = [[0,1],[0,-1],[-1,0],[1,0]]

        while True:
            r,c = choice(heading)
            row_t = self.row + r
            col_t = self.col + c
            val = maze[row_t][col_t]
            if  val == 0 or val == 2:
                return [r,c]

    def move(self):
        if self.canMove():
            self.row += self.heading[0]
            self.col += self.heading[1]
        else:
            self.heading = self.getRandomHeading()


    def draw(self):
        pos = (self.col*30, self.row*30)
        self.window.blit(self.img, pos)

class Food(character):

    def draw(self):
        center = (self.col*30+15,self.row*30+15)
        pygame.draw.circle(self.window,food['color'],center,food['radius'],food['width'])

def createGhosts(window, n):
    lst = []
    for i in range(n):
        ghost = Ghost(window,3,8)
        lst.append(ghost)
    return lst


    