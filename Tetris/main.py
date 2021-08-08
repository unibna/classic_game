import pygame
import threading
import random
import time
from config import *

from window import Window
from brick import Dot, Brick

class Tetris:

    running = True
    window_size = [525,660]

    def run(self):
        self.setup()

        self.loop()
    
    def setup(self):
        pygame.init()

        # create window
        self.screen = Window(self.window_size)
        self.draw_dot = Dot(self.screen)

        # create game board
        self.screen.create_game_board()

        # create brick
        ## brick type value is from 0 to 6
        ## should be set to 0 in default
        self.brick = Brick(self.screen, 0, 0, 0, 1)
 
    def loop(self):

        while self.running:
            # re-draw game board
            self.brick.erase()
            self.update_game_board()

            self.bind_event()

            # auto moving
            time.sleep(frame_val)
            if self.brick.can_move_down():
                self.brick.move_down()
                self.brick.draw()
            else:
                self.brick.update_matrix()
                for line in matrix:
                    print(line)
                self.reset_brick()
                continue

            # update frame
            pygame.display.flip()
    
    def bind_event(self):
        for event in pygame.event.get():
            # quit game conditions
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYUP:
                key_name = event.key

                if key_name == pygame.K_d or key_name == pygame.K_RIGHT:
                    if self.brick.can_move_right():
                        self.brick.move_right()
                elif key_name == pygame.K_a or key_name == pygame.K_LEFT:
                    if self.brick.can_move_left():
                        self.brick.move_left()
                elif key_name == pygame.K_s or key_name == pygame.K_DOWN:
                    if self.brick.can_move_down():
                        self.brick.move_down()
                elif key_name == pygame.K_w or key_name == pygame.K_UP:
                    new_brick = self.brick.create_rotated_brick()
                    if self.brick.can_rotate(new_brick):
                        self.brick.rotate(new_brick)
    
    ## brick logic handle functions
    def reset_brick(self):
        new_brick_type = random.randint(0,6)
        new_color_id = random.randint(0,len(brick_colors)-1)
        self.brick.set_brick(new_brick_type,new_color_id,0,4)

    def update_game_board(self):
        self.screen.create_game_board()
        for row in range(22,2,-1):
            for col in range(1,11):
                val = matrix[row][col]
                if val == 0:
                    continue
                
                print(f'[Tetris] Update {val}-({row},{col})')
                self.draw_dot.color_id = val - 1
                self.draw_dot.set_coor(row,col)
                self.draw_dot.draw()
        print("="*30)

    def is_goal_lines(self):
        pass

game = Tetris()
game.run()

