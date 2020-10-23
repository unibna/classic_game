from config import *
from random import randint

class Dot:

	def __init__(self, window, row = None, col = None, is_head=0):
		self.window = window
		self.row = row
		self.col = col
		self.color = None
		self.is_head = is_head

	def draw(self):
		if self.is_head:
			self.color = snake['head color']
		else:
			self.color = snake['dot color']

		rect = pygame.Rect(self.col*grid['size']+2,self.row*grid['size']+2,snake['size'],snake['size'])
		pygame.draw.rect(self.window, self.color, rect, 0)

	def get_pos(self):
		return (self.row,self.col)

class Food(Dot):

	def __init__(self, window, row=None,col=None):
		super().__init__(window,row,col)
		self.color = food['type 1 color']

	def draw(self):
		half = int(grid['size']/2)
		pygame.draw.circle(
				self.window,
				self.color,
				(self.col*grid['size']+half,self.row*grid['size']+half),
				food['radius'],
				food['width']
			)

	def set_random_pos(self):
		self.row = randint(0,19)
		self.col = randint(0,19)

class Snake:

	def __init__(self, window):
		self.window = window

		# snake configures
		# heading: [row,col]
		self.heading = [0,1] 
		# the first dot (dot zero) is the head of snake
		self.dots=[
			Dot(window,5,5,1), 
			Dot(window,5,4),
			Dot(window,5,3)
		]

	def draw(self):
		for dot in self.dots:
			dot.draw()

	def get_head_pos(self):
		return self.dots[0].get_pos()

	def append(self):
		row,col = self.dots[0].get_pos()
		dot = Dot(self.window,row,col)
		self.dots.insert(0, dot)

	def can_move(self):
		new_row = self.dots[0].row + self.heading[0]
		new_col = self.dots[0].col + self.heading[1]

		if (new_row >=0 and new_row <= 19) and (new_col >=0 and new_col <= 19):
			return [new_row, new_col]

		return None

	def move(self):
		result = self.can_move()
		if result != None:
			# set up head dot
			dot = self.dots.pop(len(self.dots)-1)
			dot.row = result[0]
			dot.col = result[1]
			dot.is_head = 1

			# replace old head
			self.dots[0].is_head = 0
			self.dots.insert(0, dot)

	def move_right(self):
		if self.heading != [0,-1]:
			self.heading = [0,1]

	def move_left(self):
		if self.heading != [0,1]:
			self.heading = [0,-1]

	def move_up(self):
		if self.heading != [1,0]:
			self.heading = [-1,0]

	def move_down(self):
		if self.heading != [-1,0]:
			self.heading = [1,0]







