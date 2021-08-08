import pygame
from config import *

class Window:

    # This class used to create and manage game board, next-brick board, and score board.
    game_board_cor = (space,space)

    def __init__(self,size):
        self.wd = pygame.display.set_mode(size)

    def create_components(self):
        self.create_game_board()
        self.create_score_board()
        self.create_next_board()

    def create_game_board(self):
        left = space
        top = space

        # draw game board
        rect = pygame.Rect(left,top,
                            game_width,game_height)
        pygame.draw.rect(self.wd, colors['game_bg'], rect)

        # draw grid lines
        # horizontal
        for row in range(21):
            pygame.draw.line(self.wd, colors['game_line'], (space,space+row*cell_size), (space+game_width,space+row*cell_size))
        # vertical
        for col in range(11):
            pygame.draw.line(self.wd, colors['game_line'], (space+col*cell_size,space), (space+col*cell_size,space+game_height))
            
    def create_score_board(self):
        pass 

    def create_next_board(self):
        pass 
