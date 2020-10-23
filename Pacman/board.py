from config import *

BORDER_DIR = os.path.join(IMAGE_DIR,"Border")

class Board:

    """
        Board is created based on 2D Maze
        Each value of maze's element corresponse one shape
        0 : None
        1 : Obstacles
        2 : Food
    """

    def __init__(self, window, maze):
        self.window = window
        self.maze = maze
        self.loadImage()
        self.config()

    def config(self):
        self.window.fill(window['color'])

        self.drawMaze()

    def loadImage(self):
        self.images = {
            # Line
            'horizontal_line': pygame.image.load(os.path.join(BORDER_DIR,'horizontal_line.png')),
            'vertical_line': pygame.image.load(os.path.join(BORDER_DIR,'vertical_line.png')),
            # Point
            'point_up': pygame.image.load(os.path.join(BORDER_DIR,'point_up.png')),
            'point_down': pygame.image.load(os.path.join(BORDER_DIR,'point_down.png')),
            'point_right': pygame.image.load(os.path.join(BORDER_DIR,'point_right.png')),
            'point_left': pygame.image.load(os.path.join(BORDER_DIR,'point_left.png')),
            # Corner
            'corner_lu': pygame.image.load(os.path.join(BORDER_DIR,'corner_lu.png')),
            'corner_ld': pygame.image.load(os.path.join(BORDER_DIR,'corner_ld.png')),
            'corner_ru': pygame.image.load(os.path.join(BORDER_DIR,'corner_ru.png')),
            'corner_rd': pygame.image.load(os.path.join(BORDER_DIR,'corner_rd.png')),
            # Cross
            'cross': pygame.image.load(os.path.join(BORDER_DIR,'cross.png')),
            # T line
            't_left': pygame.image.load(os.path.join(BORDER_DIR,'t_left.png')),
            't_right': pygame.image.load(os.path.join(BORDER_DIR,'t_right.png')),
            't_down': pygame.image.load(os.path.join(BORDER_DIR,'t_down.png')),
            't_up': pygame.image.load(os.path.join(BORDER_DIR,'t_up.png')),
        }

    def drawMaze(self):
        rowlen = len(self.maze)
        collen = len(self.maze[0])

        for row in range(rowlen):
            for col in range(collen):
                if self.maze[row][col] == 0:
                    continue
                elif self.maze[row][col] == 1:
                    key = self.hanldeObstacles(row,col)
                    pos = (col*30,row*30)
                    self.window.blit(self.images[key],pos)

    def hanldeObstacles(self,row,col):  
        heading = [[0,1],[0,-1],[-1,0],[1,0]] # r l u d
        rst = []

        for i in range(4):
            r,c = heading[i]
            row_t = row + r
            col_t = col + c
            try:
                if maze[row_t][col_t] == 1:
                    rst.append(i)
            except:
                continue
        
        if 0 in rst and 1 in rst:
            if 2 in rst and 3 in rst:
                return 'cross'
            elif 2 in rst:
                return 't_up'
            elif 3 in rst:
                return 't_down'
            else:
                return 'horizontal_line'
        elif 2 in rst and 3 in rst:
            if 0 in rst:
                return 't_right'
            elif 1 in rst:
                return 't_left'
            else:
                return 'vertical_line'
        elif 0 in rst:
            if 2 in rst:
                return 'corner_ru'
            elif 3 in rst:
                return 'corner_rd'
            else:
                return 'point_left'
        elif 1 in rst:
            if 2 in rst:
                return 'corner_lu'
            elif 3 in rst:
                return 'corner_ld'
            else:
                return 'point_right'
        elif 2 in rst:
            return 'point_down'
        elif 3 in rst:
            return 'point_up'



            
        
    

