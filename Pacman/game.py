from config import *

from board import Board
from character import Pacman, Food, createGhosts

from time import sleep

class Game:

    is_running = True
    fps = 7.5
    score = 0

    window = pygame.display.set_mode(window['size'])
    clock = pygame.time.Clock()
    board = Board(window, maze)

    pacman = Pacman(window,1,1)
    ghosts = createGhosts(window, 4)
    food   = Food(window)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pacman')

    def start(self):
        sleep(2)
        # Loop
        self.loop()

    def loop(self):
        while self.is_running:

            self.bindEvent()
            self.clearBoard()


            # Pacman
            self.pacman.move()
            if self.pacman.eat():
                self.score += 1
                print(self.score)
            #Ghost
            for ghost in self.ghosts:
                ghost.move()
                if ghost.getPos() == self.pacman.getPos():
                    print("Lose")
                    return
            # Food
            self.updateFood()

            # Draw
            self.pacman.draw()
            for ghost in self.ghosts:
                ghost.draw()

            self.clock.tick(self.fps)
            pygame.display.update()

    def clearBoard(self):
        self.window.fill(window['color'])
        self.board.drawMaze()

    def bindEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.pacman.moveDown()
                elif event.key == pygame.K_UP:
                    self.pacman.moveUp()
                elif event.key == pygame.K_RIGHT:
                    self.pacman.moveRight()
                elif event.key == pygame.K_LEFT:
                    self.pacman.moveLeft()

    def updateFood(self):
        for row in range(rowlen):
            for col in range(collen):
                if maze[row][col] == 2:
                    self.food.row = row
                    self.food.col = col
                    self.food.draw()

if __name__ == "__main__":
    game = Game()    
    game.start()
