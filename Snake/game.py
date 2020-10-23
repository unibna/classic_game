from config import *
from snake import Snake, Food

from time import sleep

class SnakeGame:

	# attributes
	is_running = True
	fps = 10

	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Snake Game')
		self.window = pygame.display.set_mode((window['size']))
		self.clock = pygame.time.Clock()
		self.snake = Snake(self.window)
		self.food = Food(self.window,10,10)

	def start(self):
		# loop
		self.loop()

	def loop(self):
		while self.is_running:

			# refesh window
			self.clear()

			# catch events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.is_running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						self.snake.move_right()
					elif event.key == pygame.K_LEFT:
						self.snake.move_left()
					elif event.key == pygame.K_DOWN:
						self.snake.move_down()
					elif event.key == pygame.K_UP:
						self.snake.move_up()

			# food
			self.food.draw()						

			# snake move
			self.snake.move()
			# draw snake
			self.snake.draw()

			# check if snake eat food
			if self.snake.get_head_pos() == self.food.get_pos():
				self.snake.append()
				self.food.set_random_pos()

			self.clock.tick(self.fps)
			pygame.display.update()

	def draw_grid(self):
		row_len = int(board['width']/grid['size'])
		col_len = int(board['height']/grid['size'])

		# draw vertical lines
		for col in range(col_len + 1):
			pygame.draw.line(
				self.window,
				grid['color'],
				(0, col*grid['size']),
				(board['height'], col*grid['size']),
				grid['width']
				)

		# draw horizontal lines
		for row in range(row_len + 1):
			pygame.draw.line(
				self.window,
				grid['color'],
				(row*grid['size'], 0),
				(row*grid['size'], board['width']),
				grid['width']
				)

	def clear(self):
		# fill all window
		self.window.fill(window['background color'])
		# draw grid (refesh board game)
		self.draw_grid()


if __name__ == '__main__':
	game = SnakeGame()
	game.start()