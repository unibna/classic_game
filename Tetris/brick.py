import pygame 
from config import *

from window import Window

class Dot:
    
    def __init__(self, window:Window, color_id = None, row = None, col = None):
        self.window = window
        self.row = row
        self.col = col 
        self.color_id = color_id

    def set_new_dot(self,color_id,row,col):
        self.row = row
        self.col = col 
        self.color_id = color_id

    def set_coor(self, row, col):
        self.row = row
        self.col = col

    def draw(self):
        if self.row <= 2:
            return 

        left = self.window.game_board_cor[0] + (self.col-1)*cell_size + cell_border
        top = self.window.game_board_cor[1] + (self.row-3)*cell_size + cell_border

        rect = pygame.Rect(left,top,
                            cell_size-cell_border,cell_size-cell_border)
        pygame.draw.rect(self.window.wd, brick_colors[self.color_id], rect)

    def erase(self):
        if self.row <= 2:
            return 

        left = self.window.game_board_cor[0] + (self.col-1)*cell_size
        top = self.window.game_board_cor[1] + (self.row-3)*cell_size + cell_border

        rect = pygame.Rect(left,top,
                            cell_size,cell_size)
        pygame.draw.rect(self.window.wd, colors['game_bg'], rect)

    def is_empty(self):
        if self.row == None or self.col == None:
            return True
        return False

    def update_matrix(self):
        if matrix[self.row][self.col] == 0:
            matrix[self.row][self.col] = self.color_id + 1

    def can_move_right(self):
        if matrix[self.row][self.col+1] != 0:
            return False

        return True

    def can_move_left(self):
        if matrix[self.row][self.col-1] != 0:
            return False

        return True

    def can_move_down(self):
        if matrix[self.row+1][self.col] != 0:
            # print(f'[Dot] Hold ({self.row+1},{self.col} = {matrix[self.row+1][self.col]})')
            return False

        return True

    def move_right(self):
        self.col += 1

    def move_left(self):
        self.col -= 1

    def move_down(self):
        self.row += 1
        # print(f'[Dot] Move down ({self.row},{self.col})')

class Brick:

    dots = []

    def __init__(self, window:Window, brick_type = None, color_id = None, row = None, col = None):
        self.window = window
        self.row = row
        self.col = col 
        self.color_id = color_id
        self.brick = brick_types[brick_type]

        self.setup()

    def setup(self):
        # create dot list
        for i in range(4):
            new_dot = Dot(self.window)
            self.dots.append(new_dot)

        self.set_dots_cor()

    def set_brick(self,brick_type, color_id, row, col):
        self.row = row
        self.col = col 
        self.color_id = color_id
        self.brick = brick_types[brick_type]
        self.set_dots_cor()

    def set_dots_cor(self):
        # set the coordinate for each dot
        index = 0
        for r in range(len(self.brick)):
            for c in range(len(self.brick[r])):
                if self.brick[r][c] == 1:
                    self.dots[index].set_new_dot(self.color_id,self.row+r,self.col+c)
                    index += 1
                    if index == 4:
                        return

    def set_brick_type(self, br_type):
        self.brick = brick_types[br_type]
        self.set_dots_cor()

    def set_coor(self, row, col):
        self.row = row
        self.col = col

    def draw(self):
        for dot in self.dots:
            # check if dot is empty
            if dot.is_empty():
                print(f'[Error] Dot is empty.')
                return
            dot.draw()

    def erase(self):
        for dot in self.dots:
            if dot.is_empty():
                print(f'[Error] Dot is empty.')
                return
            dot.erase()

    def update_matrix(self):
        for dot in self.dots:
            dot.update_matrix()
            print(f'[Brick] Dot update ({dot.row},{dot.col})')
        print("="*30)

    def can_move_right(self):
        for dot in self.dots:
            if not dot.can_move_right():
                return False
        return True
    
    def can_move_left(self):
        for dot in self.dots:
            if not dot.can_move_left():
                return False
        return True

    def can_move_down(self):
        for dot in self.dots:
            if not dot.can_move_down():
                return False
        return True

    def move_right(self):      
        for dot in self.dots:
            dot.move_right()
        self.col += 1
            
    def move_left(self):
        for dot in self.dots:
            dot.move_left()
        self.col -= 1

    def move_down(self):
        for dot in self.dots:
            dot.move_down()
        self.row += 1         
        # print(f'[Brick] Move down ({self.row},{self.col})')   

    def create_rotated_brick(self):
        row_len = len(self.brick)
        col_len = len(self.brick[0])

        # new_row_len = col_len
        # new_col_len = row_len
        new_brick = []

        for col in range(col_len):
            new_row = []
            for row in range(row_len):
                new_row.append(self.brick[row][col])
            new_brick.append(new_row[::-1])
        
        return new_brick

    def can_rotate(self, new_brick):
        for r in range(len(new_brick)):
            for c in range(len(new_brick[0])):
                if matrix[self.row+r][self.col+c] != 0:
                    return False

        return True

    def rotate(self, new_brick):
        self.brick = new_brick
        self.set_dots_cor()


        

